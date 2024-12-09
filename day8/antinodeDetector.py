import numpy as np

data = []

with open("test.txt", "r") as file:
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
    for i in range(1, len(coords)):
        neighbor_x, neighbor_y = coords[i]
        x_dif = x - neighbor_x
        y_dif = y - neighbor_y
        if not((x_dif + x >= x_max or y_dif + y >= y_max) or (x_dif + x < 0 or y_dif + y < 0)):
            output.append(((x_dif + x),(y_dif + y)))
        if not((x - 2 * x_dif >= x_max or y - 2 * y_dif >= y_max) or (x - 2 * x_dif < 0 or y - 2 * y_dif < 0)):
            output.append(((x - 2 * x_dif),(y - 2 * y_dif)))
    return find_antinodes(coords[1:], output)

output = []
for list in locations:
    antinodes = []
    output = output + find_antinodes(list, antinodes)
output = set(output)

print(output)
print(len(output))
for coords in output:
    np_map[coords[0], coords[1]] = '#'