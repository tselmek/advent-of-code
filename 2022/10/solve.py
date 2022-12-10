from typing import List

lines = [line.rstrip("\n") for line in open("input.txt")]

LINE_SIZE = 40

X = 1
tick = 0
strength = 0

def add_tick():
  global tick, strength

  y, x = tick // 40, tick % 40
  screen[y][x] = "█" if abs(X - x) <= 1 else " "

  tick += 1
  if (tick - 20) % 40 == 0:
    strength += tick * X

screen = [
  ["" for _ in range(40)]
  for _ in range(6)
]

for line in lines:
  if "noop" in line:
    add_tick()
    continue

  if "addx" in line:
    n = int(line.split(" ")[1])
    add_tick()
    add_tick()
    X += n


print(strength)

for line in screen:
  print("".join(line))