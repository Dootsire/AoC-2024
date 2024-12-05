import numpy as np

text_array = []
with open("data.txt","r") as file:
    for line in file.readlines():
        text_array.append(list(line.strip()))

np_array = np.array(text_array)

coords = np.where(np_array == 'X')
y_coords = coords[0]
x_coords = coords[1]
matches = len(x_coords)
remaining_pattern = ['M', 'A', 'S']
count = 0

def find_pattern_count(y, x):
    count = 0
    directions = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]
    for offset in directions:
        end = [offset[0]*3 + y,offset[1]*3 + x]
        if (end[0] < 0 or end[0] >= np_array.shape[0]) or (end[1] < 0 or end[1] >= np_array.shape[1]):
            continue
        if (np_array[offset[0] + y, offset[1] + x] == remaining_pattern[0]
            ) and (np_array[offset[0]*2 + y, offset[1]*2 + x] == remaining_pattern[1]
            ) and (np_array[offset[0]*3 + y, offset[1]*3 + x] == remaining_pattern[2]):
            count += 1
    return count
    

for i in range(matches):
    count += find_pattern_count(y_coords[i], x_coords[i])
print(count)