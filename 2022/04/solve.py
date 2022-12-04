from typing import List


lines = [
  list(map(int, line.rstrip("\n").replace("-", ",").split(",")))
  for line in open("example.txt")
]

ranges = [
  ((start1, end1), (start2, end2))
  for start1, end1, start2, end2 in lines
]

def number_of_contained_ranges(ranges: List[str]) -> int:
  n = 0

  for range1, range2 in ranges:
    s1, e1 = range1
    s2, e2 = range2
    if s1 <= s2 <= e2 <= e1: # On check si range2 est dans range1
      n += 1
      continue
    if s2 <= s1 <= e1 <= e2: # On check si range1 est dans range2
      n += 1
      continue

  return n 


def number_of_overlapping_ranges(ranges: List[str]) -> int:
  n = 0

  for range1, range2 in ranges:
    s1, e1 = range1
    s2, e2 = range2
    if s2 <= s1 <= e2 or s1 <= s2 <= e1:
      n += 1

  return n 

print(number_of_contained_ranges(ranges))

print(number_of_overlapping_ranges(ranges))

