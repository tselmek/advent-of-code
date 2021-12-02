
lines = [int(line.rstrip("\n")) for line in open("input.txt")]

def number_of_increases(window_size: int = 1) -> int:
    n = sum(
        lines[k+window_size] > lines[k]
        for k in range(len(lines)-window_size)
    )
    return n

print(number_of_increases(1))

print(number_of_increases(3))