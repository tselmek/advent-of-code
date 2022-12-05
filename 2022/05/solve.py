from typing import List, Tuple
import re


lines = [line.rstrip("\n") for line in open("input.txt")]

space = lines.index("")

stacks_input = lines[:space]
moves_input = lines[space+1:]

def parse_stacks(stacks_input: List[str]) -> List[List[str]]:
  number_of_stacks = int(stacks_input[-1].split(" ")[-2])
  stacks = [[] for _ in range(number_of_stacks)]

  for stack_line in reversed(stacks_input[:-1]):
    for stack_index in range(number_of_stacks):
      crate = stack_line[1 + 4 * stack_index]
      if crate == " ":
        continue
      stacks[stack_index].append(crate)
  
  return stacks


def extract_move_instructions(instruction: str) -> Tuple[int, int, int]:
    crates, from_stack, to_stack = map(int, re.search(r"move (\d+) from (\d+) to (\d+)", instruction).groups())
    from_stack -= 1
    to_stack -= 1
    
    return crates, from_stack, to_stack


def move_crates_with_cratemover9000(stacks_input: List[str], moves_input: List[str]) -> List[List[str]]:
  stacks = parse_stacks(stacks_input)

  # Handle moves
  for move in moves_input:
    crates, from_stack, to_stack = extract_move_instructions(move)
    for _ in range(crates):
      stacks[to_stack].append(stacks[from_stack].pop())
  
  return stacks



def move_crates_with_cratemover9001(stacks_input: List[str], moves_input: List[str]) -> List[List[str]]:
  stacks = parse_stacks(stacks_input)

  # Handle moves
  for move in moves_input:
    crates, from_stack, to_stack = extract_move_instructions(move)
    stacks[to_stack].extend(stacks[from_stack][-crates:])
    del stacks[from_stack][-crates:]
  
  return stacks


def build_result_string(stacks: List[List[str]]) -> str:
  return "".join(stack[-1] for stack in stacks)


stacks_9000 = move_crates_with_cratemover9000(stacks_input, moves_input)
print(build_result_string(stacks_9000))

stacks_9001 = move_crates_with_cratemover9001(stacks_input, moves_input)
print(build_result_string(stacks_9001))
