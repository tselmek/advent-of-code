import numpy as np


lines = [line.rstrip("\n") for line in open("input.txt")]

octopuses = [
    [
        int(c) for c in line
    ]
    for line in lines
]

NUMBER_OF_STEPS = 100
HEIGHT = len(octopuses)
WIDTH = len(octopuses[0])

step = 0
flashes = 0
first_sync_flash = None

while not first_sync_flash:

    flash = []
    step += 1

    for i in range(HEIGHT):
        for j in range(WIDTH):
            octopuses[i][j] += 1
            if octopuses[i][j] == 10:
                flash.append( (i, j) )
    
    while len(flash) > 0:
        i, j = flash.pop(0)
        flashes += 1
        octopuses[i][j] = 0
        neighbors = [
            (i-1, j-1), (i-1, j), (i-1, j+1),
            (i  , j-1),           (i  , j+1),
            (i+1, j-1), (i+1, j), (i+1, j+1)
        ]
        for ni, nj in neighbors:
            if 0 <= ni < HEIGHT and 0 <= nj < WIDTH:
                if octopuses[ni][nj] not in [0, 10]:
                    octopuses[ni][nj] += 1
                    if octopuses[ni][nj] == 10:
                        flash.append( (ni, nj) )
    
    if step == NUMBER_OF_STEPS:
        print(flashes)
    
    sync_flash = np.sum(octopuses) == 0
    if sync_flash:
        first_sync_flash = step


print(first_sync_flash)