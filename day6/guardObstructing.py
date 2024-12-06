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
marking_dict = {
    '^':'U',
    '>':'R',
    'v':'D',
    '<':'L'
}

in_bounds = True
i = 0
rows, cols = np_map.shape

while(True):
    location = np.argwhere(np_map==direction)[0]
    distance = direction_distance_dict.get(direction)
    new_location = (location[0] + distance[0], location[1] + distance[1])

    if (new_location[0] < 0 or new_location[0] >= rows) or (
        new_location[1] < 0 or new_location[1] >= cols):
        np_map[location[0], location[1]] = 'X'
        break

    if (np_map[new_location] == '#'):
        direction = changing_directions_dict.get(direction)
        np_map[location[0], location[1]] = direction
    else:
        np_map[new_location] = direction
        np_map[location[0], location[1]] = 'X'

step_map = np.argwhere(np_map == 'X').tolist()
np_map = np.array(map_data)
starting_loc = np.argwhere(np_map == '^')[0].tolist()
step_map.remove(starting_loc)

count = 0

for step in step_map:
    obstacle_dict = {}
    test_map = np.array(np_map)
    test_map[step[0],step[1]] = '#'
    direction = '^'
    while(True):
        location = np.argwhere(test_map==direction)[0]
        distance = direction_distance_dict.get(direction)
        new_location = (location[0] + distance[0], location[1] + distance[1])

        if (new_location[0] < 0 or new_location[0] >= rows) or (
            new_location[1] < 0 or new_location[1] >= cols):
            break

        if (test_map[new_location] == '#'):
            if new_location in obstacle_dict:
                if direction in obstacle_dict[new_location]:
                    count += 1
                    break
                obstacle_dict[new_location].append(direction)
            else:
                obstacle_dict[new_location] = [direction]
            direction = changing_directions_dict.get(direction)
            test_map[location[0], location[1]] = direction
        else:
            test_map[new_location] = direction
            test_map[location[0], location[1]] = '.'
    print(step, count)

print(count)