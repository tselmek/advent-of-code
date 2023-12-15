import regex as re

lines = [line.rstrip("\n") for line in open("input.txt")]

init_sequence = lines[0].split(",")

def hash(s):
  current_value = 0

  for c in s:
    current_value += ord(c)
    current_value *= 17
    current_value %= 256
  
  return current_value


def boot_system(init_sequence):
  return sum(map(hash, init_sequence))


def focusing_power(box, slot, focal_length):
  return (box + 1) * (slot + 1) * focal_length


def boot_system_2(init_sequence):
  boxes = [{} for _ in range(256)]

  for step in init_sequence:
    match = re.match(r"^([a-z]+)(-|=\d)$", step)
    
    label, instruction = match[1], match[2]
    box = hash(label)

    if instruction == "-":
      if label in boxes[box]:
        del boxes[box][label]
    
    if instruction.startswith("="):
      boxes[box][label] = int(instruction[1])
  
  return sum(
    focusing_power(box, slot, focal_length)
    for box, lenses in enumerate(boxes)
    for slot, focal_length in enumerate(lenses.values())
  )


print(boot_system(init_sequence))

print(boot_system_2(init_sequence))
