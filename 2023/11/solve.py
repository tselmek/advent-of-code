
UNIVERSE = [line.rstrip("\n") for line in open("input.txt")]

EMPTY_SPOT = "."
GALAXY_SPOT = "#"


def find_emptiness(universe):
  empty_lines = [k for k, row in enumerate(universe) if set(row) == {EMPTY_SPOT}]
  empty_columns = [k for k in range(len(universe[0])) if set([row[k] for row in universe]) == {EMPTY_SPOT}]

  return empty_lines, empty_columns


def get_empty_crossings(galaxy1, galaxy2, empty_lines, empty_columns):
  galaxy1_i, galaxy1_j = galaxy1
  galaxy2_i, galaxy2_j = galaxy2

  cross_empty_lines = [
    empty_line
    for empty_line in empty_lines
    if empty_line > min(galaxy1_i, galaxy2_i) and empty_line < max(galaxy1_i, galaxy2_i)
  ]
  cross_empty_columns = [
    empty_column
    for empty_column in empty_columns
    if empty_column > min(galaxy1_j, galaxy2_j) and empty_column < max(galaxy1_j, galaxy2_j)
  ]
  empty_crossings = len(cross_empty_lines) + len(cross_empty_columns)

  return empty_crossings

def compute_galaxy_distances(universe, expansion_rate = 1):
  galaxies = [
    (i, j)
    for i in range(len(UNIVERSE))
    for j in range(len(UNIVERSE[0]))
    if UNIVERSE[i][j] == GALAXY_SPOT
  ]

  empty_lines, empty_columns = find_emptiness(universe)

  total_distances = 0

  for k, (galaxy_i, galaxy_j) in enumerate(galaxies):
    for (neighbor_i, neighbor_j) in galaxies[k+1:]:
      empty_crossings = get_empty_crossings((galaxy_i, galaxy_j), (neighbor_i, neighbor_j), empty_lines, empty_columns)
      distance = abs(galaxy_i - neighbor_i) + abs(galaxy_j - neighbor_j) + empty_crossings * (expansion_rate - 1)

      total_distances += distance
  
  return total_distances


print(compute_galaxy_distances(UNIVERSE, 1))

print(compute_galaxy_distances(UNIVERSE, 1_000_000))