
from typing import List, Tuple


lines = [line.rstrip("\n") for line in open("input.txt")]

heightmap = [[int(c) for c in line] for line in lines]

def is_low_point(heightmap: List[List[int]], i: int, j: int) -> bool:
    point = heightmap[i][j]
    left = heightmap[i][j-1] > point if j > 0 else True 
    right = heightmap[i][j+1] > point if j < len(heightmap[0])-1 else True 
    top = heightmap[i-1][j] > point if i > 0 else True 
    bottom = heightmap[i+1][j] > point if i < len(heightmap)-1 else True

    return left and right and top and bottom

risk_levels = []
for i, line in enumerate(heightmap):
    risk_levels.append([])
    for j, spot in enumerate(line):
        risk_levels[i].append(
            (spot + 1) * is_low_point(heightmap, i, j)
        )

print(sum(sum(line) for line in risk_levels))

def neighbor_spots(heightmap: List[List[int]], i: int, j: int) -> List[Tuple[int, int]]:
    neighbors = []
    if i > 0:
        neighbors.append((i-1, j))
    if i < len(heightmap)-1:
        neighbors.append((i+1, j))
    if j > 0:
        neighbors.append((i, j-1))
    if j < len(heightmap[0])-1:
        neighbors.append((i, j+1))
    return [(ni, nj) for (ni, nj) in neighbors if heightmap[ni][nj] != 9]

unexplored_spots = [(i, j) for i in range(len(heightmap)) for j in range(len(heightmap[0]))]
bassin = []
tailles_bassin = []

while len(unexplored_spots) > 0:
    bassin = [unexplored_spots.pop(0)]
    tailles_bassin.append(0)

    while len(bassin) > 0:
        i, j = bassin.pop(0)

        if heightmap[i][j] != 9:
            tailles_bassin[-1] += 1
            for ni, nj in neighbor_spots(heightmap, i, j):
                if (ni, nj) in unexplored_spots:
                    bassin.append((ni, nj))
                    unexplored_spots.pop(unexplored_spots.index((ni, nj)))

bassins = sorted(tailles_bassin, reverse=True)
print(bassins[0] * bassins[1] * bassins[2])
