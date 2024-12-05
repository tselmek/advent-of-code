import re

lines = [line.rstrip("\n") for line in open("input.txt")]

orders = [list(map(int, line.split("|"))) for line in lines if re.match(r"^\d+\|\d+$", line)]
updates = [list(map(int, line.split(","))) for line in lines if re.match(r"^\d+(,\d+)*$", line)]

AFTER = {}
for before, after in orders:
  if before not in AFTER:
    AFTER[before] = []
  if after not in AFTER:
    AFTER[after] = []
  AFTER[before].append(after)


def filter_updates_in_correct_order(updates):
  order_checks = [
    (
      update,
      [all([uwu in AFTER[u] for uwu in update[i+1:]]) for i, u in enumerate(update)]
    )
    for update in updates
  ]

  return sum([
    update[len(update)//2]
    for update, order_check in order_checks
    if all(order_check)
  ])


print(filter_updates_in_correct_order(updates))
