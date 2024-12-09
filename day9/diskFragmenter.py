import re

def string_to_disk_layout(file):
    count = 0
    layout = []
    while True:
        char = file.read(1)
        if not char:
            break
        layout += full_or_empty(char, count)
        count += 1
    return layout

def full_or_empty(char, count):
    num = int(char)
    output = []
    if (count % 2 == 0):
        output += num_to_id(num, count // 2)
    else:
        output += num_to_space(num)
    return output

def num_to_id(num, id):
    output = []
    for i in range(num):
        output += [id]
    return output

def num_to_space(num):
    output = []
    for i in range(num):
        output += ['.']
    return output

def replace_space_with_id(layout):
    space_index = find_space(layout)
    id_index = find_last_id(layout)
    layout[space_index] = layout[id_index]
    layout[id_index] = '.'

def find_space(layout):
    for i in range(len(layout)):
        if layout[i] == '.':
            return i

def find_last_id(layout):
    for i in range(len(layout) - 1, 0, -1):
        if isinstance(layout[i], int):
            return i

def check_if_completed(layout):
    complete = False
    if find_space(layout) > find_last_id(layout):
        complete = True
    return complete

def calc_checksum(layout):
    pass

with open("data.txt", "r", encoding="utf-8") as file:
    disk_layout = string_to_disk_layout(file)
while not(check_if_completed(disk_layout)):
    replace_space_with_id(disk_layout)

stripped_layout = disk_layout[:find_space(disk_layout)]
output = 0
for i in range(len(stripped_layout)):
    output += stripped_layout[i] * i
print(output)