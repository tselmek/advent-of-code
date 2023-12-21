import regex as re

lines = [line.rstrip("\n") for line in open("example.txt")]

separation = lines.index("")

workflows = lines[:separation]
parts = lines[separation + 1:]

WORKFLOWS = {}
PARTS = []
FIRST_WORFLOW = "in"

for workflow in workflows:
  match = re.match(r"^([^\{]+)\{([^\}]+)\}$", workflow)
  name = match[1] 
  rules = [rule.split(":") for rule in match[2].split(",")]

  WORKFLOWS[name] = rules

for part in parts:
  match = re.match(r"^\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}$", part)
  PARTS.append({
    "x": int(match[1]),
    "m": int(match[2]),
    "a": int(match[3]),
    "s": int(match[4])
  })


def apply_workflow(part, workflow):
  for rule in workflow[:-1]:
    if eval(rule[0], part):
      return rule[1]
  
  return workflow[-1][0]

def process_part(part):
  workflow = FIRST_WORFLOW

  while workflow not in "AR":
    workflow = apply_workflow(part, WORKFLOWS[workflow])
  
  return workflow

def compute_accepted_parts(parts):
  total = 0

  for part in parts:
    if process_part(part) == "A":
      total += part["x"] + part["m"] + part["a"] + part["s"]

  return total



print(compute_accepted_parts(PARTS))
