import re

pos_list = []
vel_list = []
y_limit = 103
x_limit = 101
quadrants = [0,0,0,0]

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

def calc_quadrant(point):
    y_divide = (y_limit - 1) // 2
    x_divide = (x_limit - 1) // 2
    if (point[0] < x_divide):
        if (point[1] < y_divide):
            quadrants[0] += 1
        elif (point[1] > y_divide):
            quadrants[1] += 1
    elif (point[0] > x_divide):
        if (point[1] < y_divide):
            quadrants[2] += 1
        elif (point[1] > y_divide):
            quadrants[3] += 1

with open("data.txt", "r") as file:
    for line in file.readlines():
        numbers = re.findall(r'-?[0-9]+', line.strip())
        ints = [int(x) for x in numbers]
        pos_list.append(ints[0:2])
        vel_list.append(tuple(ints[2:4]))

for i in range(100):
    move_by_a_second()

for pos in pos_list:
    calc_quadrant(pos)

output = 1
for quad in quadrants:
    output *= quad
print(output)