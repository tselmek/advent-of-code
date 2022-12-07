from typing import List

lines = [line.rstrip("\n") for line in open("input.txt")]


def parse_command(line: str) -> bool:
  is_input = line[0] == "$"
  command = line[2:] if is_input else line
  args = command.split(" ")
  if args[0].isnumeric():
    return "file", int(args[0]), args[1]
  return args[0], args[1] if args[0] != "ls" else None


def get_dir(system: dict, path: List[str]) -> dict:
  directory = system
  for target in path:
    directory = directory[target]
  return directory


def total_size(directory: dict) -> int:
  directory["total"] = directory["files"]
  for folder in directory:
    if folder not in ["total", "files"]:
      directory["total"] += total_size(directory[folder])
  return directory["total"]


def sum_over(directory: dict) -> int:
  somme = 0
  if directory["total"] <= FOLDER_MAX_SIZE:
    somme += directory["total"]
  for folder in directory:
    if folder not in ["total", "files"]:
      somme += sum_over(directory[folder])
  return somme


def deletable_folder(directory: dict) -> int:
  children_sizes = [
    deletable_folder(directory[folder])
    for folder in directory 
    if folder not in ["files", "total"]
  ]

  deletable_sizes = [
    size
    for size in children_sizes
    if size >= NEEDED_SPACE
  ]

  if len(deletable_sizes) == 0:
    return 0 if directory["total"] < NEEDED_SPACE else directory["total"]

  return min(deletable_sizes)


SYSTEM = {
  "/": {
    "files": 0
  }
}

FOLDER_MAX_SIZE = 100_000
SYSTEM_SIZE = 70_000_000
UPDATE_SPACE = 30_000_000

current_directory = SYSTEM["/"]
current_path = ["/"]

for line in lines:
  args = parse_command(line)
  match args[0]:
    case "file":
      current_directory["files"] += args[1]
    case "ls":
      pass
    case "cd":
      if args[1] == "..":
        current_path.pop()
        current_directory = get_dir(SYSTEM, current_path)
      elif args[1] == "/":
        current_path = ["/"]
        current_directory = SYSTEM["/"]
      else:
        current_path.append(args[1])
        current_directory = current_directory[args[1]]
    case "dir":
      if args[1] not in current_directory:
        current_directory[args[1]] = {"files": 0}

ROOT_SIZE = total_size(SYSTEM["/"])
FREE_SPACE = SYSTEM_SIZE - ROOT_SIZE
NEEDED_SPACE = UPDATE_SPACE - FREE_SPACE


print(sum_over(SYSTEM["/"]))

print(deletable_folder(SYSTEM["/"]))