import csv

def is_increasing(row):
    prev_value = row[0]
    for entry in row[1:]:
        if entry <= prev_value:
            return False
        prev_value = entry
    return True

def is_decreasing(row):
    prev_value = row[0]
    for entry in row[1:]:
        if entry >= prev_value:
            return False
        prev_value = entry
    return True

def min_distance(row, distance):
    prev_value = row[0]
    for entry in row[1:]:
        distance = abs(prev_value - entry)
        if (distance > 3):
            return False
        prev_value = entry
    return True

data = []

with open('data.csv', 'r') as read_obj: 
    csv_reader = csv.reader(read_obj)
    data = [[int(items) for items in row if items != ''] for row in csv_reader]

count = 0
unfit_data = []


for row in data:
    if ((is_increasing(row) or is_decreasing(row))
        and min_distance(row, 3)):
        count += 1
    else:
        unfit_data.append(row)

print(count)

for row in unfit_data:
    for i in range(len(row)):
        new_row = row[:i] + row[i+1:]
        if ((is_increasing(new_row) or is_decreasing(new_row))
            and min_distance(new_row, 3)):
            count += 1
            break

print(count)