from typing import List 


lines = [line.rstrip("\n") for line in open("input.txt")]


def parse_elves_calories(calories: List[str]) -> List[int]:
    elves = [0]
    for calory in calories:
        if calory == "":
            elves.append(0)
            continue
        elves[-1] += int(calory)
    return elves

def sum_of_most_calories(elves: List[int], top: int) -> int:
    sorted_elves = sorted(elves, reverse=True)
    return sum(sorted_elves[:top])


elves = parse_elves_calories(lines)

print(sum_of_most_calories(elves, 1))

print(sum_of_most_calories(elves, 3))