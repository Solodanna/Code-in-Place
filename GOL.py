import os

print("Welcome you in the Conway's Game of Life!")
print()
print("The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:")
print("1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.")
print("2. Any live cell with two or three live neighbours lives on to the next generation.")
print("3. Any live cell with more than three live neighbours dies, as if by overpopulation.")
print("4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.")
print()

# The begining. @ represents a live cell. space represents a dead cell.
"""seed = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "@", "@", "@", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]"""
seed = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "@", " ", " ", "@", " ", " ", " "],
    [" ", " ", "@", " ", "@", "@", " ", "@", " ", " "],
    [" ", " ", " ", "@", " ", " ", "@", " ", " ", " "],
    [" ", " ", " ", "@", " ", " ", "@", " ", " ", " "],
    [" ", " ", "@", " ", "@", "@", " ", "@", " ", " "],
    [" ", " ", " ", "@", " ", " ", "@", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
#Next generation
gen = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]

# Dimensions of grid is 10 X 10
first_index = 0
last_index = 10

while True:
    input("Press 'Enter' to continue.")
    os.system("clear")

    for x in range (first_index, last_index):
        for y in range (first_index, last_index):
            print(seed[x][y], end = " ")
        print()

    for x in range (first_index, last_index):
        for y in range (first_index, last_index):
            # Checking the neighbours #
            neighbours = 0
            for x1 in range (-1, 2):
                for y1 in range (-1, 2):
                    if x1 != 0 or y1 != 0:
                        x2 = x + x1
                        y2 = y + y1

                        # When index is out the range - check the cells on the oposite board od the grid. The gris is a thor #
                        if x2 < first_index:
                            x2 = last_index - 1
                        elif x2 == last_index:
                            x2 = first_index
                        if y2 < first_index:
                            y2 = last_index - 1
                        elif y2 == last_index:
                            y2 = first_index

                        if seed[x2][y2] == "@":
                            neighbours += 1

            if neighbours == 3 or neighbours == 2 and seed[x][y] == "@":
                gen[x][y] = "@"
            else:
                gen[x][y] = " "
    
    for x in range (first_index, last_index):
        for y in range (first_index, last_index):
            seed[x][y] = gen[x][y]
            gen[x][y] = " "

