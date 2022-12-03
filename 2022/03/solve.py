from typing import List, Tuple


lines = [line.rstrip("\n") for line in open("input.txt")]

a = 1
A = 27

def priority(character: str) -> int:
  if character.isupper():
    return A + ord(character) - ord("A")

  return a + ord(character) - ord("a")

def sum_compartment_priorities(lines: List[str]) -> int:
  sum_priorities = 0

  for line in lines:
    half = len(line) // 2
    compartment1 = set(line[:half])
    compartment2 = set(line[half:])
    common = compartment1.intersection(compartment2)
    sum_priorities += priority(list(common)[0])

  return sum_priorities

print(sum_compartment_priorities(lines))

def sum_elves_priorities(lines: List[str]) -> int:
  sum_priorities = 0

  for k in range(0, len(lines), 3):
    elves = [
      set(lines[k+kk]) for kk in [0, 1, 2]
    ]
    common = set.intersection(*elves)
    sum_priorities += priority(list(common)[0])
  
  return sum_priorities

print(sum_elves_priorities(lines))

