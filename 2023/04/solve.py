import regex as re

lines = [line.rstrip("\n") for line in open("input.txt")]

def process_lines(lines):
  processed_lines = []

  for line in lines:
    card, winning_numbers, numbers = re.search(r"^Card\s+(\d+): ([^\|]*) \| ([^\|]*)", line).groups()

    winning_numbers = set(winning_numbers.split(" "))
    if "" in winning_numbers:
      winning_numbers.remove("")
    
    numbers = set(numbers.split(" "))
    if "" in numbers:
      numbers.remove("")
    
    matching_numbers = winning_numbers.intersection(numbers)
  
    processed_lines.append((int(card), winning_numbers, numbers, matching_numbers))
  
  return processed_lines


def compute_score(lines):
  total_score = 0

  cards = process_lines(lines)

  for _, _, _, matching_numbers in cards:
    if len(matching_numbers) > 0:
      total_score += 2 ** (len(matching_numbers) - 1)

  return total_score


def compute_scratchcards(lines):

  cards = process_lines(lines)

  victory = {
    card: [card + k for k in range(1, len(matching_numbers) + 1)]
    for card, _, _, matching_numbers in cards
  }

  won_cards = [card for card, _, _, _ in cards]
  current_card = 0

  while current_card < len(won_cards):
    won_cards.extend(victory[won_cards[current_card]])
    current_card += 1

  return len(won_cards)

print(compute_score(lines))

print(compute_scratchcards(lines))
