import numpy as np

data = []

with open("data.txt", "r") as file:
    for line in file.readlines():
        chars = list(line.strip())
        data.append([int(x) for x in chars])

np_map = np.array(data)
directions = [
    [0,1],
    [0,-1],
    [1,0],
    [-1,0]
]
max_row, max_col = np_map.shape
top = 9

def find_end(coords, target):
    paths = []
    if (len(coords) == 0):
        return 0
    for coord in coords:
        for dir in directions:
            row, col = coord[0] + dir[0], coord[1] + dir[1]
            valid = ((row >= 0 and row < max_row) and (col >= 0 and col < max_col))
            if (valid and (np_map[row, col] == target)):
                paths.append((row, col))
    new_target = target + 1
    if (target != top):
        return find_end(set(paths), new_target)
    else:
        return len(set(paths))

zeroes = np.argwhere(np_map == 0)
output = 0
for zero in zeroes:
    output += find_end([zero], 1)
print(output)