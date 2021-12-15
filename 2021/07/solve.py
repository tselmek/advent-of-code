
from os import posix_fadvise
from typing import Callable, List


lines = [line.rstrip("\n") for line in open("input.txt")]

crabs = list(map(int, lines[0].split(",")))


def constant_fuel_function(crab_position: int, goal_position: int) -> int:
    return abs(crab_position - goal_position)

def linear_fuel_function(crab_position: int, goal_position: int) -> int:
    n = abs(crab_position - goal_position)
    return n * (n + 1) // 2


def optimal_crab_fuel(crabs: List[int], fuel_function: Callable[[int, int], int]) -> int:

    min_crab, max_crab = min(crabs), max(crabs)

    min_fuel = None

    for position in range(min_crab, max_crab):
        total_fuel = sum(fuel_function(crab, position) for crab in crabs)

        if min_fuel == None or total_fuel < min_fuel:
            min_fuel = total_fuel 
        
    return min_fuel


print(optimal_crab_fuel(crabs, constant_fuel_function))

print(optimal_crab_fuel(crabs, linear_fuel_function))

