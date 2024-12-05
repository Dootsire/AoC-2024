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

for row in data:
    if ((is_increasing(row) or is_decreasing(row))
        and min_distance(row, 3)):
        count += 1

print(count)