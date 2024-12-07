import re

lines = [line.rstrip("\n") for line in open("input.txt")]
lines = [re.findall(r"^(\d+): (\d+(?: \d+)+)$", line) for line in lines]
lines = [(int(line[0][0]), list(map(int, line[0][1].split(" ")))) for line in lines]


def apply_operator(operator, a, b):
  match operator:
    case "*":
      return a * b
    case "+":
      return a + b
    case "|":
      return int(str(a) + str(b))

def is_target_in_possible_values(numbers, target, include_concatenation=False):
  possible_values = [numbers[0]]
  operators = "*+|" if include_concatenation else "*+"

  for number in numbers[1:]:
    new_values = []
    for operation in operators:
      for value in possible_values:
        new_value = apply_operator(operation, value, number)
        new_values.append(new_value)
    possible_values = new_values[:]

  return target in possible_values

def compute_total_calibration_result(calibrations, include_concatenation=False):
  total = 0

  for calibration in calibrations:
    target, numbers = calibration
  
    if is_target_in_possible_values(numbers, target, include_concatenation):
      total += target
  
  return total


print(compute_total_calibration_result(lines))

print(compute_total_calibration_result(lines, include_concatenation=True))