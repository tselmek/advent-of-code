import regex as re
import portion as P

lines = [line.rstrip("\n") for line in open("input.txt")]


def is_number_in_mapping(number, mapping):
  destination_range_start, source_range_start, range_length = mapping

  return number >= source_range_start and number < source_range_start + range_length


def get_number_mapping(number, mappings):
  for mapping in mappings:
    if is_number_in_mapping(number, mapping):
      return mapping

  return None


def compute_destination_number(number, mappings):
  mapping = get_number_mapping(number, mappings)

  if mapping is None:
    return number

  destination_range_start, source_range_start, range_length = mapping

  return destination_range_start + (number - source_range_start)

def parse_mappings(lines):
  mappings = []

  for line in lines[2:]:
    map_start = re.match(r"^(\w+)-to-(\w+) map:", line)

    if map_start:
      mappings.append([])
      continue

    mapping = re.match(r"^(\d+) (\d+) (\d+)", line)

    if mapping:
      mappings[-1].append(tuple(map(int, mapping[0].split(" "))))

  return mappings

PARSED_SEEDS = re.match(r"seeds: (.*)", lines[0]).groups()
PARSED_SEEDS = list(map(int, PARSED_SEEDS[0].split(" ")))

PARSED_MAPPINGS = parse_mappings(lines)

def compute_lowest_location_part1(parsed_seeds):
  seeds = parsed_seeds[:]

  for M in PARSED_MAPPINGS:
    seeds = list(map(lambda n: compute_destination_number(n, M), seeds))

  lowest_location = min(seeds)
  return lowest_location



# def get_intersection_interval(seed_range, mappings):
#   for mapping, delta in mappings:
#     if seed_range.overlaps(mapping):
#       return (mapping, delta)

#   return None

# def apply_mapping_to_seed_range(seed_range, source, Delta):
#   mapped = seed_range & source
#   untouched = seed_range - mapped

#   mapped = mapped.replace(lower=lambda x: x + Delta, upper=lambda x: x + Delta)

#   return mapped | untouched

# def compute_destination_range(seed_range, mappings):
#   intersection_interval = get_intersection_interval(seed_range, mappings)

#   if intersection_interval is None:
#     return seed_range

#   mapping, delta = intersection_interval

#   return apply_mapping_to_seed_range(seed_range, mapping, delta)


# def compute_lowest_location_part2(parsed_seeds):
#   seed_ranges = list(zip(*(iter(parsed_seeds),) * 2))
#   seed_ranges = [P.closed(start, start + length - 1) for start, length in seed_ranges]

#   mappings = [
#     [
#       (P.closed(source_start, source_start + length - 1), destination_start - source_start)
#       for destination_start, source_start, length in parsed_mappings
#     ]
#     for parsed_mappings in PARSED_MAPPINGS
#   ]

#   for M in mappings:
#     seed_ranges = list(map(lambda r: compute_destination_range(r, M), seed_ranges))
  
#   lowest_location = min(seed_ranges, key=lambda r: r.lower)

#   return lowest_location.lower


print(compute_lowest_location_part1(PARSED_SEEDS))

# Part 2 is not working yet, answer is corect on example.txt but too low on input.txt
# print(compute_lowest_location_part2(PARSED_SEEDS))

