char_dict = {}

def insert_into_dict(char, coords):
    if (char in char_dict):
        find_group(char, coords)
    else:
        add_set(char,coords)

def find_group(char, coords):
    directions = [(coords[0] + 1, coords[1]), (coords[0], coords[1] + 1),
                  (coords[0] - 1, coords[1]), (coords[0], coords[1] - 1)]
    added = False
    for dir in directions:
        for i, char_set in enumerate(char_dict.get(char)):
            if dir in char_set:
                char_set.add(coords)
                added = True
    if added == False:
        add_set(char, coords)

def add_set(char, coords):
    new_set = set()
    new_set.add(coords)
    if char in char_dict:
        char_dict[char].append(new_set)
    else:
        char_dict[char] = [new_set]

def combine_like_sets(set_list):
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(set_list):
            j = i + 1
            while j < len(set_list):
                if not set_list[i].isdisjoint(set_list[j]):
                    set_list[i].update(set_list[j])
                    set_list.pop(j)
                    changed = True
                else:
                    j += 1
            i += 1

def calc_sides(char_set):
    for coords in char_set:
        check_sides(coords, char_set)
    sides = 0
    for set_list in side_dict.values():
        combine_like_sets(set_list)
        sides += len(set_list)
    return sides

def check_sides(coords, char_set):
    directions = [[(-1,0), (0,1), (0,-1)],
                  [(1,0), (0,1), (0,-1)],
                  [(0,-1), (1,0), (-1,0)],
                  [(0,1), (-1,0), (1,0)]]
    for dir in directions:
        space = (coords[0] + dir[0][0], coords[1] + dir[0][1])
        if space not in char_set:
            if len(side_dict.get(dir[0])) == 0:
                add_side_set(dir[0], coords)
            else:
                l_up = (coords[0] + dir[1][0], coords[1] + dir[1][1])
                r_up = (coords[0] + dir[2][0], coords[1] + dir[2][1])
                added = False
                for set_list in side_dict.get(dir[0]):
                    if l_up in set_list or r_up in set_list:
                        set_list.add(coords)
                        added = True
                if added == False:
                    add_side_set(dir[0], coords)

def add_side_set(side, coords):
    new_set = set()
    new_set.add(coords)
    if len(side_dict.get(side)) != 0:
        side_dict[side].append(new_set)
    else:
        side_dict[side] = [new_set]

with open("data.txt", "r") as file:
    for y, line in enumerate(file.readlines()):
        for x, char in enumerate(line.strip()):
            insert_into_dict(char, (y,x))

cost = 0
for set_list in char_dict.values():
    combine_like_sets(set_list)
    for char_set in set_list:
        side_dict = {
            (-1,0):[],
            (1,0):[],
            (0,-1):[],
            (0,1):[]
        }
        sides = calc_sides(char_set)
        cost += sides * len(char_set)

print(cost)