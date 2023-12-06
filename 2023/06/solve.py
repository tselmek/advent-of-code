import regex as re
import math


lines = [line.rstrip("\n") for line in open("input.txt")]

times = list(map(int, re.findall(r"(\d+)", lines[0])))
distances = list(map(int, re.findall(r"(\d+)", lines[1])))

def solve_quadratic(a, b, c):
  delta = b**2 - 4*a*c
  solution_1 = (-b + delta**0.5) / (2*a)
  solution_2 = (-b - delta**0.5) / (2*a)

  lower = math.ceil(min(solution_1, solution_2))
  upper = math.floor(max(solution_1, solution_2))

  return lower, upper

def compute_possible_wins(races):
  possible_wins = 1

  for time_allowed, distance_record in races:
    # Solve the equation -t^2 + t * time_allowed > distance_record for whole numbers
    p = lambda t: -t**2 + t * time_allowed
    l, u = solve_quadratic(-1, time_allowed, -distance_record)

    if p(l) <= distance_record:
      l += 1

    if p(u) <= distance_record:
      u -= 1
    
    possible_wins *= u - l + 1

  return possible_wins

RACES = [
  (times[k], distances[k]) for k in range(len(times))
]

print(compute_possible_wins(RACES))

SINGLE_RACE = [(
  int("".join(map(str, times))),
  int("".join(map(str, distances)))
)]

print(compute_possible_wins(SINGLE_RACE))
