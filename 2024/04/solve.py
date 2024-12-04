
lines = [line.rstrip("\n") for line in open("input.txt")]


def possible_words(grid, i, j, height, width):
  words = []

  if i >= 3:
    word = "".join([grid[i][j], grid[i-1][j], grid[i-2][j], grid[i-3][j]])
    words.append(word)

  if j >= 3:
    word = "".join([grid[i][j], grid[i][j-1], grid[i][j-2], grid[i][j-3]])
    words.append(word)
  
  if i <= height - 4:
    word = "".join([grid[i][j], grid[i+1][j], grid[i+2][j], grid[i+3][j]])
    words.append(word)

  if j <= width - 4:
    word = "".join([grid[i][j], grid[i][j+1], grid[i][j+2], grid[i][j+3]])
    words.append(word)

  if i >= 3 and j >= 3:
    word = "".join([grid[i][j], grid[i-1][j-1], grid[i-2][j-2], grid[i-3][j-3]])
    words.append(word)

  if i >= 3 and j <= width - 4:
    word = "".join([grid[i][j], grid[i-1][j+1], grid[i-2][j+2], grid[i-3][j+3]])
    words.append(word)

  if i <= height - 4 and j >= 3:
    word = "".join([grid[i][j], grid[i+1][j-1], grid[i+2][j-2], grid[i+3][j-3]])
    words.append(word)

  if i <= height - 4 and j <= width - 4:
    word = "".join([grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3]])
    words.append(word)

  return words

def count_xmas_words(grid):
  height = len(grid)
  width = len(grid[0])

  number_of_xmas = 0

  for i in range(height):
    for j in range(width):
      if grid[i][j] != "X":
        continue
    
      words = possible_words(grid, i, j, height, width)
      xmas = len([w for w in words if w == "XMAS"])
      number_of_xmas += xmas

  return number_of_xmas


def count_xmas_crosses(grid):
  height = len(grid)
  width = len(grid[0])

  number_of_xmas = 0
  ACCEPTED_MAS = ["MAS", "SAM"]

  for i in range(1, height - 1):
    for j in range(1, width - 1):
      if grid[i][j] != "A":
        continue

      first_diagonal = "".join([grid[i-1][j-1], grid[i][j], grid[i+1][j+1]])
      second_diagonal = "".join([grid[i+1][j-1], grid[i][j], grid[i-1][j+1]])

      if first_diagonal in ACCEPTED_MAS and second_diagonal in ACCEPTED_MAS:
        number_of_xmas += 1
  
  return number_of_xmas


print(count_xmas_words(lines))

print(count_xmas_crosses(lines))