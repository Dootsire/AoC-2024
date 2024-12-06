import numpy as np

map_data = []

with open("data.txt", "r") as file:
    for line in file.readlines():
        map_data.append(list(line.strip()))

np_map = np.array(map_data)

direction = '^'
direction_distance_dict = {
    '^':[-1,0],
    '>':[0,1],
    'v':[1,0],
    '<':[0,-1]
}
changing_directions_dict = {
    '^':'>',
    '>':'v',
    'v':'<',
    '<':'^'
}

in_bounds = True
i = 0
rows, cols = np_map.shape

while(True):
    location = np.argwhere(np_map==direction)[0]
    distance = direction_distance_dict.get(direction)
    new_location = (location[0] + distance[0], location[1] + distance[1])

    if (new_location[0] < 0 or new_location[0] > rows) or (
        new_location[1] < 0 or new_location[1] > cols):
        np_map[location[0], location[1]] = 'X'
        break

    if (np_map[new_location] == '#'):
        direction = changing_directions_dict.get(direction)
        np_map[location[0], location[1]] = direction
    else:
        np_map[new_location] = direction
        np_map[location[0], location[1]] = 'X'

print(np.count_nonzero(np_map == 'X'))