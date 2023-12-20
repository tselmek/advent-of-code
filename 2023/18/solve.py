import regex as re

lines = [line.rstrip("\n") for line in open("input.txt")]

PLAN = []
PLAN_B = []

for line in lines:
  match = re.match(r"^([RLDU]) (\d+) \((#[0-9a-f]{6})\)$", line)
  PLAN.append( (match[1], int(match[2]), match[3]) )

  distance = int(match[3][1:6], base=16)
  direction = "RDLU"[int(match[3][6])]
  PLAN_B.append( (direction, distance, None) )

STARTING_POINT = (0, 0)

def move(point, direction, distance=1):
  if direction == "R":
    return (point[0], point[1] + distance)
  elif direction == "L":
    return (point[0], point[1] - distance)
  elif direction == "U":
    return (point[0] - distance, point[1])
  elif direction == "D":
    return (point[0] + distance, point[1])
  else:
    raise Exception("Invalid direction: " + direction)

# Slower version, only works for part 1
def dig_pool(start, plan):
  current = start
  filled = set([start])
  
  # Dig outer edge
  for instruction in plan:
    direction, distance, color = instruction
    for i in range(distance):
      current = move(current, direction)
      filled.add(current)
  
  # Dig inner surface
  current = move(move(start, "R"), "D")
  visited = set(filled)
  pile = [current]

  while len(pile) > 0:
    current = pile.pop()
    visited.add(current)
    filled.add(current)

    for direction in "RLUD":
      neighbor = move(current, direction)
      if neighbor not in visited:
        pile.append(neighbor)

  return filled


def compute_shoelace_area(start, plan):
  current = start
  points = [start]
  perimeter = 0

  # Dig outer edge
  for instruction in plan:
    direction, distance, color = instruction
    current = move(current, direction, distance)
    points.append(current)
    perimeter += distance

  area = 0

  for i in range(len(points)):
    j = (i + 1) % len(points)
    area += points[i][0] * points[j][1] - points[j][0] * points[i][1]

  return abs(area) // 2 + perimeter // 2 + 1 


print(compute_shoelace_area(STARTING_POINT, PLAN))

print(compute_shoelace_area(STARTING_POINT, PLAN_B))
