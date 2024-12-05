import re

with open("data.txt", 'r') as file:
    data = file.read()

prev_string = data
string = re.sub(r'don\'t\(\).+?(do\(\)|\Z)', '', data, flags = re.DOTALL)
while prev_string != string:
    prev_string = string
    string = re.sub(r'don\'t\(\).+?(do\(\)|\Z)', '', prev_string, flags = re.DOTALL)

matches = re.findall(r'mul\([1-9][0-9]{0,2}\,[1-9][0-9]{0,2}\)', string)
concated_matches = "".join(matches)
ints = re.findall(r'[1-9][0-9]{0,2}', concated_matches)

total = 0
for i in range(int(len(ints)/2)):
    index = i * 2
    total += int(ints[index]) * int(ints[index+1])

print(total)