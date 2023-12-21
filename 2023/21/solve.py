
GRID = [line.rstrip("\n") for line in open("input.txt")]

HEIGHT = len(GRID)
WIDTH = len(GRID[0])

GARDEN = "."
ROCK = "#"
START = "S"

ROCKS = set((i, j) for i in range(HEIGHT) for j in range(WIDTH) if GRID[i][j] == ROCK)


def compute_walks(grid, steps, infinite=False):
  possible_points = set((i, j) for i in range(HEIGHT) for j in range(WIDTH) if grid[i][j] == START)

  for s in range(steps):
    new_possible_points = set()

    for point in possible_points:
      for (di, dj) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_point = (point[0] + di, point[1] + dj)

        if not infinite and new_point in ROCKS:
          continue

        if infinite and (new_point[0] % HEIGHT, new_point[1] % WIDTH) in ROCKS:
          continue

        new_possible_points.add(new_point)

    possible_points = new_possible_points
  
  return len(possible_points)


print(compute_walks(GRID, 64)) # Takes too long after 500 steps
