import re
import numpy as np

def put_button_into_list(line, list):
    numbers = re.findall('[0-9]+', line)
    list.append(tuple(int(number) for number in numbers))

def put_target_into_list(line, list):
    numbers = re.findall('[0-9]+', line)
    list.append(tuple(int(number) + 10000000000000 for number in numbers))

def calc_intersection(button_1, button_2, target):
    buttons = np.array([button_1, button_2])
    target_array = np.array(target)
    intersection = np.linalg.solve(buttons.T, target_array)
    return intersection

a_list = []
b_list = []
target_list = []

with open("data.txt", "r") as file:
    while True:
        a = file.readline()
        if (a == ''):
            break
        put_button_into_list(a, a_list)
        put_button_into_list(file.readline(), b_list)
        put_target_into_list(file.readline(), target_list)
        file.readline()

intersections = []

for index in range(len(a_list)):
    intersection = list(calc_intersection(a_list[index], b_list[index], target_list[index]))
    intersection = [round(intersection[0], 3), round(intersection[1], 3)]
    if intersection[0].is_integer() and intersection[1].is_integer():
        intersection = (int(intersection[0]), int(intersection[1]))
        intersections.append(intersection)

output = 0
for pair in intersections:
    output += pair[0] * 3 + pair[1]

print(output)