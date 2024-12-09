import numpy as np

data = []

with open("data.txt", "r") as file:
    for line in file.readlines():
        data.append(list(line.strip()))

np_map = np.array(data)
unique_values = list(np.unique(np_map))
unique_values.remove('.')

locations = []
for value in unique_values:
    locations.append(np.argwhere(np_map==value))

x_max, y_max = np_map.shape

def find_antinodes(coords, output):
    if len(coords) == 1:
        return output
    x, y = coords[0]
    output.append((x,y))
    for i in range(1, len(coords)):
        in_bounds = True
        neighbor_x, neighbor_y = coords[i]
        x_dif = x - neighbor_x
        y_dif = y - neighbor_y
        mult = 1
        while in_bounds:
            x_plus = x_dif * mult + x
            y_plus = y_dif * mult + y
            x_minus = x - x_dif * mult
            y_minus = y - y_dif * mult
            mult += 1
            x_plus_in_bounds = (x_plus < x_max and x_plus >= 0)
            y_plus_in_bounds = (y_plus < y_max and y_plus >= 0)
            x_minus_in_bounds = (x_minus < x_max and x_minus >= 0)
            y_minus_in_bounds = (y_minus < y_max and y_minus >= 0)
            if (x_plus_in_bounds and y_plus_in_bounds):
                output.append((x_plus, y_plus))
            if (x_minus_in_bounds and y_minus_in_bounds):
                output.append((x_minus, y_minus))
            if ((x_plus_in_bounds and y_plus_in_bounds) == False 
                and (x_minus_in_bounds and y_minus_in_bounds) == False):
                in_bounds = False
    return find_antinodes(coords[1:], output)

output = []
for list in locations:
    antinodes = []
    output = output + find_antinodes(list, antinodes)
output = set(output)

print(len(output))