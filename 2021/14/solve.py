from collections import Counter
from typing import List


lines = [line.rstrip("\n") for line in open("input.txt")]

polymer = [c for c in lines[0]]

rules = {
    line.split(" -> ")[0]: line.split(" -> ")[1] for line in lines[2:]
}

def enhance_polymer(old_polymer: List[str], steps: int) -> int:
    polymer = old_polymer[:]
    for step in range(steps):
        k = 0
        while k < len(polymer) - 1:
            segment = "".join(polymer[k:k+2])
            if segment in rules:
                polymer = polymer[:k+1] + [rules[segment]] + polymer[k+1:]
                k += 1
            k += 1
        print(step)

    elements = Counter(polymer).most_common()
    return elements[0][1] - elements[-1][1]

# print(enhance_polymer(polymer, 10)) is fast enough

# print(enhance_polymer(polymer, 40)) but this is too slow

def optimised_enhance_polymer(old_polymer: str, steps: int) -> int:
    
    augmented_rules = {
        segment: (segment[0] + element, element + segment[1])
        for segment, element in rules.items()
    }
    
    abstract_polymer = {}

    for k in range(len(old_polymer)-1):
        segment = old_polymer[k:k+2]
        abstract_polymer[segment] = abstract_polymer.get(segment, 0) + 1
    
    for _ in range(steps):
        new_polymer = {}
        for segment in augmented_rules:
            if segment in abstract_polymer:
                for new_segment in augmented_rules[segment]:
                    new_polymer[new_segment] = new_polymer.get(new_segment, 0) + abstract_polymer[segment]
        abstract_polymer = new_polymer.copy()
    
    count_elements = {}

    for segment, count in abstract_polymer.items():
        for character in segment:
            count_elements[character] = count_elements.get(character, 0) + count

    count_elements[old_polymer[0]] += 1
    count_elements[old_polymer[-1]] += 1

    for element in count_elements:
        count_elements[element] //= 2

    elements = Counter(count_elements).most_common()
    return elements[0][1] - elements[-1][1]


print(optimised_enhance_polymer("".join(polymer), 10))

print(optimised_enhance_polymer("".join(polymer), 40))