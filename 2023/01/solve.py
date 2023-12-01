import regex as re


lines = [line.rstrip("\n") for line in open("input.txt")]

SIMPLE_DIGITS = r"(\d)"
SPELLED_OUT_DIGITS = r"(\d|one|two|three|four|five|six|seven|eight|nine)"
TRANSLATE_DIGITS = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9"
}

def compute_calibration_values(lines, part=1):
  total = 0
  regex = SIMPLE_DIGITS if part == 1 else SPELLED_OUT_DIGITS

  for line in lines:
    numbers = re.findall(regex, line, overlapped=True)
    
    first_digit = TRANSLATE_DIGITS.get(numbers[0], numbers[0])
    last_digit = TRANSLATE_DIGITS.get(numbers[-1], numbers[-1])
    
    total += int(first_digit + last_digit)

  return total


print(compute_calibration_values(lines, part=2))