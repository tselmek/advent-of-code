
line = [line.rstrip("\n") for line in open("input.txt")][0]


def build_memory_part1(disk_map):
  memory = []
  index = 0
  space = "file"

  for c in disk_map:
    match space:
      case "file":
        for _ in range(int(c)):
          memory.append(index)
        space = "empty"
        index += 1

      case "empty":
        for _ in range(int(c)):
          memory.append(".")
        space = "file"
  
  return memory

def rearrange_memory_part1(memory):
  empty_indices = [k for k, e in enumerate(memory) if e == "."]
  file_indices = [k for k, f in enumerate(memory) if f != "."]

  while empty_indices[0] < file_indices[-1]:
    e_index = empty_indices.pop(0)
    f_index = file_indices.pop()

    memory[e_index], memory[f_index] = memory[f_index], memory[e_index]

  return memory

def compute_memory_checksum_part1(disk_map):
  memory = build_memory_part1(disk_map)
  rearrange_memory_part1(memory)

  return sum([
    k * space for k, space in enumerate(memory) if space != "."
  ])



def build_memory_part2(disk_map):
  memory = [
    [k // 2 if k % 2 == 0 else ".", int(d)] for k, d in enumerate(disk_map)
  ]
  memory = [
    m for m in memory if m[1] > 0
  ]
  
  return memory

def flatten_empty_slots(memory):
  k = 1

  while k < len(memory):
    if memory[k-1][0] == memory[k][0] == ".":
      memory[k-1][1] += memory[k][1]
      memory.pop(k)
    else:
      k += 1

def rearrange_memory_part2(memory):
  max_file = max([m for m in memory if m[0] != "."], key=lambda m: m[0])
  max_index = max_file[0]

  while max_index > 0:
    possible_empty_indices = list(filter(lambda m: m[0] == "." and m[1] >= max_file[1], memory))

    # print("Empty", possible_empty_indices)

    if len(possible_empty_indices) == 0:
      max_index -= 1
      max_file = max([m for m in memory if m[0] != "." and m[0] <= max_index], key=lambda m: m[0])
      continue

    first_empty_slot = possible_empty_indices[0]
    f_index = [k for k, m in enumerate(memory) if m == max_file][0]
    e_index = [k for k, m in enumerate(memory) if m == first_empty_slot][0]

    if e_index >= f_index:
      max_index -= 1
      max_file = max([m for m in memory if m[0] != "." and m[0] <= max_index], key=lambda m: m[0])
      continue

    # print("Swapping", "empty at", e_index, "and file at", f_index)

    filled_size = max_file[1]
    remaining_size = first_empty_slot[1] - filled_size

    if remaining_size == 0:
      memory[e_index], memory[f_index] = memory[f_index], memory[e_index]

    if remaining_size > 0:
      memory[e_index][1] = filled_size
      memory[e_index], memory[f_index] = memory[f_index], memory[e_index]
      memory.insert(e_index + 1, [".", remaining_size])
    
    flatten_empty_slots(memory)
    
    # print(max_index, ":", "".join([m[1] * str(m[0]) for m in memory]))
    max_index -= 1
    max_file = max([m for m in memory if m[0] != "." and m[0] <= max_index], key=lambda m: m[0])


  return memory

def compute_memory_checksum_part2(disk_map):
  memory = build_memory_part2(disk_map)
  rearrange_memory_part2(memory)

  memory = "".join([m[1] * str(m[0]) for m in memory])

  return sum([
    k * int(space) for k, space in enumerate(memory) if space != "."
  ])


print(compute_memory_checksum_part1(line))

# Finds right answer on example but wrong answer on input :'(
print(compute_memory_checksum_part2(line))
