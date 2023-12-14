
from time import perf_counter
import numpy as np

GRID = [
  [c for c in line.rstrip("\n")]
  for line in open("input.txt")
]

EMPTY = "."
ROUNDED_ROCK = "O"
CUBE_ROCK = "#"
ROCKS = "O#"

HEIGHT = len(GRID)

ROUNDED_ROCKS = [
  (i, j)
  for i in range(len(GRID))
  for j in range(len(GRID[0]))
  if GRID[i][j] == ROUNDED_ROCK
]

CUBE_ROCKS = [
  (i, j)
  for i in range(len(GRID))
  for j in range(len(GRID[0]))
  if GRID[i][j] == CUBE_ROCK
]

def compute_stop(rock, direction):
  tstart = perf_counter()
  i, j = rock

  if direction == "N":
    up = i - 1 
    while up >= 0 and GRID[up][j] not in ROCKS:
      up -= 1
    stop = up + 1
    return (stop, j)

  if direction == "S":
    down = i + 1
    while down < len(GRID) and GRID[down][j] not in ROCKS:
      down += 1
    stop = down - 1
    return (stop, j)

  if direction == "W":
    left = j - 1
    while left >= 0 and GRID[i][left] not in ROCKS:
      left -= 1
    stop = left + 1
    return (i, stop)

  if direction == "E":
    right = j + 1
    while right < len(GRID[0]) and GRID[i][right] not in ROCKS:
      right += 1
    stop = right - 1
    return (i, stop)
  
  tstop = perf_counter()
  # print("{:.2e}".format(tstop-tstart))

  return stop

def sort_rocks(rocks, direction):
  if direction == "N":
    rocks.sort(key=lambda rock: rock[0])
  elif direction == "S":
    rocks.sort(key=lambda rock: rock[0], reverse=True)
  elif direction == "W":
    rocks.sort(key=lambda rock: rock[1])
  elif direction == "E":
    rocks.sort(key=lambda rock: rock[1], reverse=True)


def tilt(rounded_rocks, direction):
  sort_rocks(rounded_rocks, direction)
  
  for k, (i, j) in enumerate(rounded_rocks):
    if direction == "W" and j == 0:
      continue
    elif direction == "E" and j == len(GRID[0]) - 1:
      continue
    elif direction == "N" and i == 0:
      continue
    elif direction == "S" and i == HEIGHT - 1:
      continue

    stop = compute_stop((i, j), direction)
    rounded_rocks[k] = stop
    GRID[i][j] = EMPTY
    GRID[stop[0]][stop[1]] = ROUNDED_ROCK

    # print((i, j), "moved to", rounded_rocks[k])


def compute_north_load(rocks):
  return sum(HEIGHT - i for i, _ in rocks)


# tilt(ROUNDED_ROCKS, "N")
# print("Result", compute_north_load(ROUNDED_ROCKS))

def part1(rocks):
  tilt(rocks, "N")
  return compute_north_load(rocks)

def part2(rocks, cycles):

  previous_configs = [set(rocks)]

  for cycle in range(1, cycles + 1):
    tilt(rocks, "N")
    tilt(rocks, "W")
    tilt(rocks, "S")
    tilt(rocks, "E")

    if set(rocks) in previous_configs:
      cycle_length = len(previous_configs) - previous_configs.index(set(rocks))
      break
    else:
      previous_configs.append(set(rocks))
  
  remaining_cycles = (cycles - cycle) % cycle_length

  for _ in range(remaining_cycles):
    tilt(rocks, "N")
    tilt(rocks, "W")
    tilt(rocks, "S")
    tilt(rocks, "E")

  return compute_north_load(rocks)


print(part1(ROUNDED_ROCKS))


CYCLES = 1_000_000_000

print(part2(ROUNDED_ROCKS, CYCLES))