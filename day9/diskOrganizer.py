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
    return layout, count // 2

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

def replace_space_with_id(layout, id):
    id_index = find_id(layout, id)
    space_start = find_remaining_space(layout, id_index)
    if (space_start == -1):
        return

    for i in range(id_index[1] - id_index[0] + 1):
        layout[space_start + i] = layout[id_index[0] + i]
        layout[id_index[0] + i] = '.'

def find_remaining_space(layout, id_index):
    space = id_index[1] - id_index[0] + 1
    space_found = 0
    index = -1
    for i in range(id_index[0]):
        if index == -1 and layout[i] == '.':
            index = i
        if layout[i] == '.':
            space_found += 1
        else:
            space_found = 0
            index = -1
        if space_found == space:
            return index
    return -1

def find_id(layout, id):
    index = [0,0]
    for i in range(len(layout) - 1, 0, -1):
        if index[1] == 0 and layout[i] == id:
            index[1] = i
        if index[1] != 0 and layout[i] != id:
            index[0] = i + 1
            return index

with open("data.txt", "r", encoding="utf-8") as file:
    disk_layout, id_count = string_to_disk_layout(file)
for i in range(id_count,0,-1):
    replace_space_with_id(disk_layout, i)

output = 0
count = 0
for entry in disk_layout:
    if entry != '.':
        output += entry * count
    count += 1
print(output)