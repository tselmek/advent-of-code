import regex as re
from math import lcm

lines = [line.rstrip("\n") for line in open("input.txt")]

WALK = lines[0]

INTERSECTIONS = {}

for line in lines[2:]:
  match = re.match(r"^([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)$", line)
  if match:
    INTERSECTIONS[match[1]] = {"L": match[2], "R": match[3]}


def compute_camel_steps(walk, intersections):
  steps = 0
  current_spot = "AAA"
  d = 0
  next_direction = walk[d]

  while current_spot != "ZZZ":
    current_spot = intersections[current_spot][next_direction]
    d += 1
    d %= len(walk)
    next_direction = walk[d]
    steps += 1

  return steps


def find_ghost_path_length(starting_spot, walk, intersections):
  current_spot = starting_spot
  d = 0
  steps = 0
  next_direction = walk[d]

  while current_spot[2] != "Z":
    current_spot = intersections[current_spot][next_direction]
    d += 1
    d %= len(walk)
    next_direction = walk[d]
    steps += 1

  return steps


def compute_ghost_steps(walk, intersections):
  starting_spots = [spot for spot in intersections if spot[2] == "A"]

  ghost_steps = [
    find_ghost_path_length(spot, walk, intersections)
    for spot in starting_spots
  ]

  return lcm(*ghost_steps)


print(compute_camel_steps(WALK, INTERSECTIONS))

print(compute_ghost_steps(WALK, INTERSECTIONS))