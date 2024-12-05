import numpy as np

text_array = []
with open("data.txt","r") as file:
    for line in file.readlines():
        text_array.append(list(line.strip()))

np_array = np.array(text_array)

coords = np.where(np_array == 'M')
y_coords = coords[0]
x_coords = coords[1]
matches = len(x_coords)
pattern = ['M', 'A', 'S']
count = 0

def find_pattern_count(y, x):
    count = 0
    directions = [[1,1], [1,-1], [-1,1], [-1,-1]]
    for offset in directions:
        end = [offset[0]*2 + y,offset[1]*2 + x]
        if (end[0] < 0 or end[0] >= np_array.shape[0]) or (end[1] < 0 or end[1] >= np_array.shape[1]):
            continue
        second_letter = np_array[offset[0] + y, offset[1] + x]
        third_letter = np_array[offset[0]*2 + y, offset[1]*2 + x]
        crossed_letter_a = np_array[offset[0]*2 + y, x]
        crossed_letter_b = np_array[y, offset[1]*2 + x]
        if (second_letter == pattern[1]) and (third_letter == pattern[2]) and ((
            crossed_letter_a == pattern[0] and crossed_letter_b == pattern[2]) or (
                crossed_letter_a == pattern[2] and crossed_letter_b == pattern[0])):
            count += 1
    return count

for i in range(matches):
    count += find_pattern_count(y_coords[i], x_coords[i])
print(count/2)