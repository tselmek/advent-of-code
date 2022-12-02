from typing import List, Tuple


lines = [line.rstrip("\n") for line in open("input.txt")]

strategy = [
  line.split(" ") for line in lines
]

# X for Rock, Y for Paper, and Z for Scissors
PLAYER_MOVE = {
  "X": "A", "Y": "B", "Z": "C"
}

# A for Rock, B for Paper, and C for Scissors
# SCORE[opponent][player]
SCORE = {
  "A": {"A": 3, "B": 6, "C": 0},
  "B": {"A": 0, "B": 3, "C": 6},
  "C": {"A": 6, "B": 0, "C": 3}
}

MOVE_SCORE = {
  "A": 1, "B": 2, "C": 3
}

# A for Rock, B for Paper, and C for Scissors
# X lose, Y draw, Z win
# MOVE[opponent][outcome]
MOVE = {
  "A": {"X": "C", "Y": "A", "Z": "B"},
  "B": {"X": "A", "Y": "B", "Z": "C"},
  "C": {"X": "B", "Y": "C", "Z": "A"}
}

def compute_player_move(opponent_move: str, player_instruction: str, instruction: str) -> str:
  if instruction == "move":
    return PLAYER_MOVE[player_instruction]

  if instruction == "outcome":
    return MOVE[opponent_move][player_instruction]


def compute_total_score(strategy: List[Tuple[str, str]], instruction_type: str) -> int:
  score = 0

  for opponent_move, player_instruction in strategy:
    player_move = compute_player_move(opponent_move, player_instruction, instruction=instruction_type)
    score += MOVE_SCORE[player_move] + SCORE[opponent_move][player_move]

  return score

print(compute_total_score(strategy, "move"))

print(compute_total_score(strategy, "outcome"))


