
lines = [line.rstrip("\n") for line in open("input.txt")]

forest = [
  [
    int(cell)
    for cell in line
  ]
  for line in lines
]

visible_trees = 0

for i, line in enumerate(forest):
  for j, tree in enumerate(line):
    if i in [0, len(forest)-1] or j in [0, len(line)-1]:
      visible_trees += 1 
      continue
    gauche = max(tree for tree in line[:j])
    droite = max(tree for tree in line[j+1:])
    haut = max(tree for tree in [line[j] for line in forest][:i])
    bas = max(tree for tree in [line[j] for line in forest][i+1:])

    if tree > min([gauche, droite, haut, bas]):
      visible_trees += 1

print(visible_trees)


best_scenic_score = 0

for i, line in enumerate(forest):
  for j, tree in enumerate(line):
    if i in [0, len(forest)-1] or j in [0, len(line)-1]:
      continue

    gauche = 1
    col = j-1
    while 0 < col and line[col] < tree:
      gauche += 1
      col -= 1
    
    droite = 1
    col = j+1
    while col < len(line)-1 and line[col] < tree:
      droite += 1
      col += 1
    
    haut = 1
    lin = i-1
    while 0 < lin and forest[lin][j] < tree:
      haut += 1
      lin -= 1

    bas = 1
    lin = i+1
    while lin < len(forest)-1 and forest[lin][j] < tree:
      bas += 1
      lin += 1

    best_scenic_score = max(best_scenic_score, droite * gauche * haut * bas)
  
print(best_scenic_score)