from typing import List


line = list(map(int, [line.rstrip("\n")
            for line in open("input.txt")][0].split(",")))


def lanternfish_expansion(line: List[int], days: int = 18) -> int:
    lantern = [0 for _ in range(9)]

    for fish in line:
        lantern[int(fish)] += 1

    for day in range(days):
        lantern = [
            lantern[1],
            lantern[2],
            lantern[3],
            lantern[4],
            lantern[5],
            lantern[6],
            lantern[7] + lantern[0],
            lantern[8],
            lantern[0]
        ]

    return sum(lantern)


print(lanternfish_expansion(line, days=80))

print(lanternfish_expansion(line, days=256))
