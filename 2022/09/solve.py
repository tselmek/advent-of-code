from typing import Tuple

lines = [line.rstrip("\n").split(" ") for line in open("input.txt")]

moves = [
  (direction, int(length))
  for direction, length in lines
]

MOVE = {
  "R": lambda length: [length, 0],
  "U": lambda length: [0, length],
  "L": lambda length: [-length, 0],
  "D": lambda length: [0, -length]
}

def distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> int:
  return max(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]))

def sign(n: int) -> int:
  if n < 0:
    return -1
  if n > 0:
    return 1
  return 0

def move_to(point: Tuple[int, int], movement: Tuple[int, int]) -> Tuple[int, int]:
  return [
    point[0] + movement[0],
    point[1] + movement[1]
  ]

def move_towards(p: Tuple[int, int], d: Tuple[int, int]) -> Tuple[int, int]:
  return [
    p[0] + sign(d[0]-p[0]),
    p[1] + sign(d[1]-p[1])
  ]

def point_hash(point: Tuple[int, int]) -> str:
  return f"{point[0]} {point[1]}"

def cells_visited_by_end_of_rope(tail_size: int) -> int:
  visited_cells = {point_hash([0, 0])}
  rope = [[0, 0] for _ in range(tail_size+1)]

  for direction, length in moves:
    for _ in range(length):
      rope[0] = move_to(rope[0], MOVE[direction](1))
      for k, _ in enumerate(rope[1:]):
        if distance(rope[k], rope[k+1]) > 1:
          rope[k+1] = move_towards(rope[k+1], rope[k])
      visited_cells.add(point_hash(rope[k+1]))
  
  return len(visited_cells)


print(cells_visited_by_end_of_rope(1))

print(cells_visited_by_end_of_rope(9))
