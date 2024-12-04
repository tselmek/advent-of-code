import re 

lines = [line.rstrip("\n") for line in open("input.txt")]


def compute_multiplications_part1(program):
  sum_of_multiplications = 0

  for line in program:
    detected_multiplications = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)

    sum_of_multiplications += sum(
      int(a) * int(b)
      for (a, b) in detected_multiplications
    )

  return sum_of_multiplications


def compute_multiplications_part2(program):
  sum_of_multiplications = 0
  enabled = True

  for line in program:
    detected_operations = re.findall(r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))", line)

    for instruction, a, b in detected_operations:
      if enabled and instruction.startswith("mul"):
        sum_of_multiplications += int(a) * int(b)

      if enabled and instruction == "don't()":
        enabled = False

      if not enabled and instruction == "do()":
        enabled = True

  return sum_of_multiplications


print(compute_multiplications_part1(lines))

print(compute_multiplications_part2(lines))