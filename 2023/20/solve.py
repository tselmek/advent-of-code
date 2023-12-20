import regex as re
from copy import deepcopy

lines = [line.rstrip("\n") for line in open("input.txt")]

LINKS = {
  "button": ["broadcaster"]
}

STATES = {
  "broadcaster": ["broadcast"]
}

for line in lines:
  match = re.match(r"^([^\s]+) -> (.*)$", line)

  _from = match[1][1:] if match[1][0] in "%&" else match[1]
  LINKS[_from] = match[2].split(", ")

  if match[1][0] == "%":
    STATES[_from] = ["flipflop", "off"]
  
  if match[1][0] == "&":
    STATES[_from] = ["conjunction", {}]

for _from in LINKS:
  _to = LINKS[_from]
  for dest in _to:
    if dest not in STATES:
      continue
    if STATES[dest][0] == "conjunction":
      STATES[dest][1][_from] = "LOW"

def push_button(states, target=None):
  pulses = [("button", "LOW")]
  sent = {
    "HIGH": 0,
    "LOW": 0
  }
  target_reached = False

  while len(pulses) > 0:
    pulse = pulses.pop(0)

    sender, value = pulse
    receivers = LINKS[sender]
    sent[value] += len(receivers)

    if target is not None and target in receivers and value == "LOW":
      target_reached = True

    for receiver in receivers:
      if receiver not in states:
        continue

      state = states[receiver]

      if state[0] == "broadcast":
        pulses.append((receiver, value))
        continue 

      if state[0] == "flipflop":
        if value == "LOW":
          if state[1] == "off":
            state[1] = "on"
            pulses.append((receiver, "HIGH"))
          else:
            state[1] = "off"
            pulses.append((receiver, "LOW"))
        continue

      if state[0] == "conjunction":
        state[1][sender] = value

        if "LOW" in state[1].values():
          pulses.append((receiver, "HIGH"))
          continue

        pulses.append((receiver, "LOW"))
        continue

  return sent["LOW"], sent["HIGH"], target_reached


def push_button_multiple_times(original_states, n=1):
  h, l = 0, 0
  states = deepcopy(original_states)

  for _ in range(n):
    _l, _h, _ = push_button(states)
    h += _h
    l += _l

  return h * l

# Part 2 execution time is too long, the trick was not found
def push_button_until_reached(original_states, target):
  button_presses = 0
  states = deepcopy(original_states)

  while True:
    _, _, target_reached = push_button(states, target)
    button_presses += 1

    if target_reached:
      return button_presses



print(push_button_multiple_times(STATES, 1_000))

print(push_button_until_reached(STATES, "rx"))

