import re
import numpy

pos_list = []
vel_list = []
y_limit = 103
x_limit = 101

def calc_pos(pos, vel):
    pos[0] = pos[0] + vel[0]
    if pos[0] < 0:
        pos[0] = x_limit + pos[0]
    elif pos[0] >= x_limit:
        pos[0] = pos[0] - x_limit
    pos[1] = pos[1] + vel[1]
    if pos[1] < 0:
        pos[1] = y_limit + pos[1]
    elif pos[1] >= y_limit:
        pos[1] = pos[1] - y_limit

def move_by_a_second():
    for index in range(len(pos_list)):
        calc_pos(pos_list[index], vel_list[index])

with open("data.txt", "r") as file:
    for line in file.readlines():
        numbers = re.findall(r'-?[0-9]+', line.strip())
        ints = [int(x) for x in numbers]
        pos_list.append(ints[0:2])
        vel_list.append(tuple(ints[2:4]))

i = 0
while True:
    i += 1
    move_by_a_second()
    np_map = numpy.zeros((x_limit, y_limit))
    valid = True
    for pos in pos_list:
        if np_map[pos[0], pos[1]] == 1:
            valid = False
            continue
        np_map[pos[0], pos[1]] += 1
    if not valid:
        continue
    numpy.savetxt('output.txt', np_map, fmt='%2d', delimiter='')
    with open('output.txt', 'r+') as file:
        text_array = file.readlines()
        text = ''
        for line in text_array:
            text += re.sub(('0'), '.', re.sub(r'\s+', '', line)) + '\n'
        file.seek(0)
        file.write(text)
        file.truncate()
    print(i)
    inp = input()