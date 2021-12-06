import re

lines = [line.rstrip("\n") for line in open("input.txt")]

MAP_SIZE = 1000

map = [[0 for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]


def sign(x):
    return int(x/abs(x) if x != 0 else 0)


for line in lines:
    x1, y1, x2, y2 = re.search("(\d+),(\d+) -> (\d+),(\d+)", line).groups()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    delta = max(abs(x2 - x1), abs(y2 - y1)) + 1

    for d in range(delta):
        y = y1 + d * sign(y2 - y1)
        x = x1 + d * sign(x2 - x1)
        map[y][x] += 1

number_of_overlaps = sum(sum(cell >= 2 for cell in line) for line in map)

print(number_of_overlaps)
