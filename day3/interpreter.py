import re

with open("data.txt", 'r') as file:
    data = file.read()

matches = re.findall(r'mul\([1-9][0-9]{0,2}\,[1-9][0-9]{0,2}\)', data)
concated_matches = "".join(matches)
ints = re.findall(r'[1-9][0-9]{0,2}', concated_matches)

print(concated_matches)
print(ints)

total = 0
for i in range(int(len(ints)/2)):
    index = i * 2
    total += int(ints[index]) * int(ints[index+1])

print(total)