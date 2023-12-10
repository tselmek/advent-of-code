
GRID = [line.rstrip("\n") for line in open("example2.txt")]

start_i = [k for k, row in enumerate(GRID) if "S" in row][0]

START = (
  start_i,
  GRID[start_i].index("S")
)

LENGTH_GRID = [
  ["" for _ in range(len(GRID[0]))]
  for _ in range(len(GRID))
]

PIPES = {
  "|": "NS",
  "-": "EW",
  "L": "NE",
  "J": "NW",
  "7": "SW",
  "F": "SE",
  ".": "",
  "S": "NSEW"
}

def compute_neighbors(point, loop):
  i, j = point
  neighbors = []
  point_at = PIPES[GRID[i][j]]
  
  if i > 0 and "N" in point_at:
    point_from = PIPES[GRID[i-1][j]]
    if "S" in point_from:
      neighbors.append((i-1, j))

  if i < len(GRID) - 1 and "S" in point_at:
    point_from = PIPES[GRID[i+1][j]]
    if "N" in point_from:
      neighbors.append((i+1, j))

  if j > 0 and "W" in point_at:
    point_from = PIPES[GRID[i][j-1]]
    if "E" in point_from:
      neighbors.append((i, j-1))

  if j < len(GRID[0]) - 1 and "E" in point_at:
    point_from = PIPES[GRID[i][j+1]]
    if "W" in point_from:
      neighbors.append((i, j+1))
  
  neighbors = [neighbor for neighbor in neighbors if neighbor not in loop]

  return neighbors

def follow_pipe(point):
  loop = []
  pile = [(point, 0)]
  longest_length = -1

  while len(pile) > 0:
    point, length = pile.pop(0)
    loop.append(point)
    LENGTH_GRID[point[0]][point[1]] = length
    longest_length = max(longest_length, length)

    neighbors = compute_neighbors(point, loop)

    for neighbor in neighbors:
      pile.append((neighbor, length + 1))

  return loop, longest_length


def classify_spaces(loop):
  spaces = [
    (i, j) 
    for i in range(len(GRID))
    for j in range(len(GRID[0]))
    if (i, j) not in loop
  ]

  spots = [[]]


LOOP, longest_path = follow_pipe(START)
print(longest_path)