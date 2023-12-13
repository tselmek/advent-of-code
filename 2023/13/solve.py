
lines = [line.rstrip("\n") for line in open("input.txt")]

MAPS = [[]]

for line in lines:
  if line == "":
    MAPS.append([])
  else:
    MAPS[-1].append(line)

def transpose(_map):
  return [
    "".join(row[i] for row in _map)
    for i in range(len(_map[0]))
  ]

def is_reflexion_line(_map, line, smudge=False):
  reflected_lines = min(line, len(_map) - line)

  number_of_diffs = 0
  for i in range(reflected_lines):
    if _map[line - 1 - i] != _map[line + i]:
      if smudge:
        number_of_diffs += sum(1 for k in range(len(_map[0])) if _map[line - 1 - i][k] != _map[line + i][k])
      else:
        return False
  
  if smudge:
    return number_of_diffs == 1

  return True

def find_horizontal_mirror(_map, smudge=False):
  mirror_line = 1

  while mirror_line < len(_map):
    if is_reflexion_line(_map, mirror_line, smudge=smudge):
      return mirror_line
    mirror_line += 1
  
  return 0

def find_vertical_mirror(_transposed_map, smudge=False):
  mirror_column = 1

  while mirror_column < len(_transposed_map):
    if is_reflexion_line(_transposed_map, mirror_column, smudge=smudge):
      return mirror_column
    mirror_column += 1
  
  return 0


def compute_ash_number(maps, smudge=False):
  return sum(100 * find_horizontal_mirror(_map, smudge=smudge) + find_vertical_mirror(transpose(_map), smudge=smudge) for _map in maps)


print(compute_ash_number(MAPS))

print(compute_ash_number(MAPS, smudge=True))