import regex as re
from collections import Counter

lines = [line.rstrip("\n") for line in open("input.txt")]
lines = [line.split(" ") for line in lines]

GAMES = [
  (line[0], int(line[1]))
  for line in lines
]

CARDS = "23456789TJQKA"
CARDS_WITH_JOKER = "J23456789TQKA"

TYPE = {
  "five_of_a_kind": 7,
  "four_of_a_kind": 6,
  "full_house": 5,
  "three_of_a_kind": 4,
  "two_pairs": 3,
  "one_pair": 2,
  "high_card": 1,
  "none": 0
}

def card_power(card, joker=False):
  scale = CARDS_WITH_JOKER if joker else CARDS
  return scale.index(card) + 2

def hand_power(hand, joker=False):
  return [
    card_power(card, joker)
    for card in hand
  ]

def hand_type(hand, joker=False):
  _hand = Counter(hand)
  values = sorted(_hand.values(), reverse=True)

  match values:
    case [5]:
      return TYPE["five_of_a_kind"]
    
    case [4, 1]:
      if joker and _hand["J"]: 
        return TYPE["five_of_a_kind"]
      return TYPE["four_of_a_kind"]
    
    case [3, 2]:
      if joker and _hand["J"]:
        return TYPE["five_of_a_kind"]
      return TYPE["full_house"]
    
    case [3, 1, 1]:
      if joker and _hand["J"]:
        return TYPE["four_of_a_kind"]
      return TYPE["three_of_a_kind"]
    
    case [2, 2, 1]:
      if joker:
        if _hand["J"] == 2:
          return TYPE["four_of_a_kind"]
        if _hand["J"] == 1:
          return TYPE["full_house"]
      return TYPE["two_pairs"]
    
    case [2, 1, 1, 1]:
      if joker and _hand["J"]:
          return TYPE["three_of_a_kind"]
      return TYPE["one_pair"]
    
    case [1, 1, 1, 1, 1]:
      if joker and _hand["J"]:
          return TYPE["one_pair"]
      return TYPE["high_card"]

    case _:
      return TYPE["none"]


def compute_total_winnings(games, joker=False):
  sort_criteria = lambda game: (hand_type(game[0], joker=joker), hand_power(game[0], joker=joker))
  sorted_games = sorted(games, key=sort_criteria, reverse=True)
  ranked_games = list(reversed(list(enumerate(reversed(sorted_games), start=1))))

  total_winnings = sum(bid * rank for rank, (hand, bid) in ranked_games)

  return total_winnings


print(compute_total_winnings(GAMES))
print(compute_total_winnings(GAMES, joker=True))