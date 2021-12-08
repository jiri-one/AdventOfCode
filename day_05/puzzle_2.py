import numpy as np

# result of test_input.txt file have to be 12 and for input.txt it is 20500
with open("input.txt", "r") as file:
    lines_list = file.read().splitlines()

# determine size of grid and get list of coorginates
coordinates = []
highest_x = 0
highest_y = 0
for line in lines_list:
    x1 = int(line.split(" -> ")[0].split(",")[0])
    y1 = int(line.split(" -> ")[0].split(",")[1])
    x2 = int(line.split(" -> ")[1].split(",")[0])
    y2 = int(line.split(" -> ")[1].split(",")[1])
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2): # append only horizontal, vertical or diagonal line
        coordinates.append((x1, y1, x2, y2))
    if highest_x < sorted([x2, x1])[-1]:
        highest_x = sorted([x2, x1])[-1]
    if highest_y < sorted([y2, y1])[-1]:
        highest_y = sorted([y2, y1])[-1]

array = np.zeros((highest_y+1,highest_x+1), dtype=int)

for coordinate in coordinates:
    x1, y1, x2, y2 = coordinate
    if x1 == x2: # it is a vertical line
        y1, y2 = sorted([y1, y2]) # we need to sort it from smallest because of range function
        for y in range(y1, y2+1):
            array[y][x1] += 1
    elif y1 == y2: # it it is a horizontal line
        x1, x2 = sorted([x1, x2]) # we need to sort it from smallest because of range function
        for x in range(x1, x2+1):
            array[y1][x] += 1
    elif abs(x1 - x2) == abs(y1 - y2): # it is a diagonal line
        if x1 > x2:
            xs = range(x2,x1+1)
        else:
            xs = reversed(range(x1,x2+1))

        if y1 > y2:
            ys = range(y2,y1+1)
        else:
            ys = reversed(range(y1,y2+1))
        
        for x,y in zip(xs, ys):
            array[y][x] += 1

print(np.count_nonzero(array >= 2))
