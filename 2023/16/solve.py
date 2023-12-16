
GRID = [line.rstrip("\n") for line in open("input.txt")]


def beam_grid(initial_beam):
  beams = [initial_beam]

  beamed_tiles = set()

  while len(beams) > 0:
    beam = beams.pop(0)

    i, j, direction = beam

    if beam in beamed_tiles:
      continue

    beamed_tiles.add(beam)

    match direction:
      case "E":
        j += 1
      case "W":
        j -= 1
      case "N":
        i -= 1
      case "S":
        i += 1
    
    if i < 0 or i >= len(GRID) or j < 0 or j >= len(GRID[0]):
      continue
  
    match GRID[i][j]:
      case ".":
        beams.append((i, j, direction))
        pass
      case "/":
        match direction:
          case "E":
            beams.append((i, j, "N"))
          case "W":
            beams.append((i, j, "S"))
          case "N":
            beams.append((i, j, "E"))
          case "S":
            beams.append((i, j, "W"))
      case "\\":
        match direction:
          case "E":
            beams.append((i, j, "S"))
          case "W":
            beams.append((i, j, "N"))
          case "N":
            beams.append((i, j, "W"))
          case "S":
            beams.append((i, j, "E"))
      case "|":
        match direction:
          case "E":
            beams.append((i, j, "N"))
            beams.append((i, j, "S"))
          case "W":
            beams.append((i, j, "N"))
            beams.append((i, j, "S"))
          case "N":
            beams.append((i, j, "N"))
          case "S":
            beams.append((i, j, "S"))
      case "-":
        match direction:
          case "E":
            beams.append((i, j, "E"))
          case "W":
            beams.append((i, j, "W"))
          case "N":
            beams.append((i, j, "E"))
            beams.append((i, j, "W"))
          case "S":
            beams.append((i, j, "E"))
            beams.append((i, j, "W"))


  energized_tiles = set([
    (i, j)
    for i, j, direction in beamed_tiles
  ])

  return len(energized_tiles) - 1


def find_optimal_initial_beam():
  left_beams = [
    (i, -1, "E")
    for i in range(len(GRID))
  ]

  right_beams = [
    (i, len(GRID[0]), "W")
    for i in range(len(GRID))
  ]

  top_beams = [
    (-1, j, "S")
    for j in range(len(GRID[0]))
  ]

  bottom_beams = [
    (len(GRID), j, "N")
    for j in range(len(GRID[0]))
  ]

  beams = left_beams + right_beams + top_beams + bottom_beams
  max_energy = 0

  for beam in beams:
    energy = beam_grid(beam)
    max_energy = max(max_energy, energy)

  return max_energy


print(beam_grid((0, -1, "E")))

print(find_optimal_initial_beam())