import regex as re


lines = [line.rstrip("\n") for line in open("input.txt")]

def compute_possible_games(lines):

  MAX_BAG = {
    "red": 12,
    "blue": 14,
    "green": 13,
  }
  
  possible_games = []

  for line in lines:
    game, subsets_line = re.search(r"^Game (\d+): (.*)", line).groups()
    subsets = subsets_line.split("; ")

    bag = {
      "red": 0,
      "blue": 0,
      "green": 0,
    }

    for subset in subsets:
      sets = subset.split(", ")
      
      for _set in sets:
        number, color = re.search(r"(\d+) (\w+)", _set).groups()
        bag[color] = max(bag[color], int(number))
    
    if bag["blue"] <= MAX_BAG["blue"] and bag["red"] <= MAX_BAG["red"] and bag["green"] <= MAX_BAG["green"]:
      possible_games.append(int(game))
    
  return possible_games


def compute_power_of_sets(lines):
  total = 0

  for line in lines:
    game, subsets_line = re.search(r"^Game (\d+): (.*)", line).groups()
    subsets = subsets_line.split("; ")

    bag = {
      "red": 0,
      "blue": 0,
      "green": 0,
    }

    for subset in subsets:
      sets = subset.split(", ")
      
      for _set in sets:
        number, color = re.search(r"(\d+) (\w+)", _set).groups()
        bag[color] = max(bag[color], int(number))
    
    total += bag["red"] * bag["blue"] * bag["green"]
  
  return total

print(sum(compute_possible_games(lines)))

print(compute_power_of_sets(lines))