

lines = [line.rstrip("\n") for line in open("input.txt")]

HISTORIES = [list(map(int, line.split(" "))) for line in lines]


def compute_sequence(history):
  return [history[k+1] - history[k] for k in range(len(history) - 1)]

def compute_next_reading(last_readings):
  return sum(last_readings)

def compute_previous_reading(first_readings):
  return sum([reading * (-1)**k for k, reading in enumerate(first_readings)])


def predict(histories):
  total_next = 0
  total_prev = 0

  for history in histories:
    sequence = history
    first_readings = [history[0]]
    last_readings = [history[-1]]

    while not all([s == 0 for s in sequence]):
      sequence = compute_sequence(sequence)

      first_readings.append(sequence[0])
      last_readings.append(sequence[-1])

    total_prev += compute_previous_reading(first_readings)
    total_next += compute_next_reading(last_readings)

  return total_next, total_prev


part1, part2 = predict(HISTORIES)

print(part1)

print(part2)