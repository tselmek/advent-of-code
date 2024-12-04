import math 

lines = [line.rstrip("\n") for line in open("input.txt")]
lines = [list(map(int, line.split(" "))) for line in lines]

def is_report_safe_part1(report):
  previous_value = report[0]
  report_sign = report[1] - report[0]

  for r in report[1:]:
    sign = r - previous_value

    if sign * report_sign <= 0:
      return False

    if abs(sign) > 3:
      return False

    previous_value = r
  
  return True


def is_report_safe_part2(report):
  previous_value = report[0]
  report_sign = report[1] - report[0]
  errors = []

  for i, r in enumerate(report[1:]):
    sign = r - previous_value

    if sign * report_sign <= 0:
      errors.append(i + 1)
    
    if abs(sign) > 3:
      errors.append(i + 1)
    
    previous_value = r
  
  for i, _ in enumerate(report):
    if is_report_safe_part1([r for j, r in enumerate(report) if j != i]):
      return True
  
  return False


def count_safe_reports(reports, is_report_safe): 
  evaluated_reports = list(map(is_report_safe, reports))

  return evaluated_reports.count(True)


print(count_safe_reports(lines, is_report_safe_part1))

print(count_safe_reports(lines, is_report_safe_part2))
