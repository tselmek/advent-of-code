
lines = [list(line.rstrip("\n")) for line in open("input.txt")]

def rotate_right(direction):
  match direction:
    case [-1, 0]:
      return [0, 1]
    case [0, 1]:
      return [1, 0]
    case [1, 0]:
      return [0, -1]
    case [0, -1]:
      return [-1, 0]

def in_front(position, direction):
  next_position = [position[0] + direction[0], position[1] + direction[1]]

  return next_position

def count_path_length(grid):
  starting_i = [i for i, line in enumerate(lines) if "^" in line][0]
  starting_j = [j for j, cell in enumerate(lines[starting_i]) if cell == "^"][0]

  height = len(grid)
  width = len(grid[0])

  guard = [starting_i, starting_j]
  direction = [-1, 0]
  length = 0

  while 0 <= guard[0] < height and 0 <= guard[1] < width:
    length += int(grid[guard[0]][guard[1]] != "X")
    grid[guard[0]][guard[1]] = "X"

    next_position = in_front(guard, direction)
    is_off_grid = next_position[0] < 0 or next_position[0] >= height or next_position[1] < 0 or next_position[1] >= width

    if is_off_grid:
      break

    if grid[next_position[0]][next_position[1]] == "#":
      direction = rotate_right(direction)
      next_position = in_front(guard, direction)
    
    guard = next_position

  return length

print(count_path_length(lines))