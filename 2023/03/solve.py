import regex as re


lines = [line.rstrip("\n") for line in open("input.txt")]
HEIGHT = len(lines)
WIDTH = len(lines[0])

def surrounding_symbols(line, start, end):
  _start = max(0, start-1)
  _end = min(end+1, WIDTH)

  symbols = ""
  if line > 0:
    upper_line = lines[line-1][_start : _end]
    symbols += "".join(upper_line)

  if start > 0:
    left_symbol = lines[line][start-1]
    symbols += left_symbol

  if end < WIDTH-1:
    right_symbol = lines[line][end]
    symbols += right_symbol

  if line < HEIGHT-1:
    lower_line = lines[line+1][_start : _end]
    symbols += "".join(lower_line)
  
  return symbols

def compute_part_numbers(lines):
  total = 0

  for k, line in enumerate(lines):
    numbers = re.finditer(r"(\d+)", line)

    for number in numbers:
      start, end = number.span()
      surrounding = surrounding_symbols(k, start, end)
      is_alone = all(s == "." for s in surrounding)

      if not is_alone:
        total += int(number.group())
  
  return total


def surrounding_numbers(all_numbers, line, start, end):
  _start = max(0, start-1)
  _end = min(end+1, WIDTH)

  numbers = []

  upper_numbers = [
    (number, (s, e)) for number, (s, e) in all_numbers[line-1] if s < _end and e > _start
  ]

  lower_numbers = [
    (number, (s, e)) for number, (s, e) in all_numbers[line+1] if s < _end and e > _start
  ]

  left_numbers = [
    (number, (s, e)) for number, (s, e) in all_numbers[line] if s <= start and e > _start
  ]

  right_numbers = [
    (number, (s, e)) for number, (s, e) in all_numbers[line] if s < _end and e >= end
  ]

  numbers.extend(upper_numbers)
  numbers.extend(lower_numbers)
  numbers.extend(left_numbers)
  numbers.extend(right_numbers)

  return [n[0] for n in numbers]


def compute_gear_ratios(lines):
  total = 0
  numbers = [
    [(int(match.group()), match.span()) for match in re.finditer(r"(\d+)", line)]
    for line in lines
  ]

  for k, line in enumerate(lines):
    gears = re.finditer(r"\*", line)

    for gear in gears:
      surrounding = surrounding_numbers(numbers, k, gear.start(), gear.end())
      if len(surrounding) == 2:
        total += surrounding[0] * surrounding[1]
  
  return total

print(compute_part_numbers(lines))

print(compute_gear_ratios(lines))
