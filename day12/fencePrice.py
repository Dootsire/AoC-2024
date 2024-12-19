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

def calc_perimeter(char_set):
    perimeter = 0
    for coords in char_set:
        directions = [(coords[0] + 1, coords[1]), (coords[0], coords[1] + 1),
                  (coords[0] - 1, coords[1]), (coords[0], coords[1] - 1)]
        for dir in directions:
            if dir not in char_set:
                perimeter += 1
    return perimeter

with open("data.txt", "r") as file:
    for y, line in enumerate(file.readlines()):
        for x, char in enumerate(line.strip()):
            insert_into_dict(char, (y,x))

cost = 0
for set_list in char_dict.values():
    combine_like_sets(set_list)
    for char_set in set_list:
        cost += calc_perimeter(char_set) * len(char_set)

'''for char, set_list in char_dict.items():
    print(char, len(set_list))
    print(set_list)'''

print(cost)