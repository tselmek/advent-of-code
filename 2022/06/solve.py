
lines = [line.rstrip("\n") for line in open("input.txt")]

message = lines[0]

def get_marker_index(packet: str) -> int:
  k = 0
  SIZE = 4 if packet == "packet" else 14

  while len(set(message[k:k+SIZE])) < SIZE:
    k += 1

  return k + SIZE

print(get_marker_index("packet"))

print(get_marker_index("message"))