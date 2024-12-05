data = []

with open("data.txt", "r") as file:
    for line in file.readlines():
        data.append(line.strip())

split = data.index('')
rules = data[:split]
data = data[split + 1:]

rules_dict = {}
for line in rules:
    rule = line.split("|")
    if rule[0] in rules_dict:
        rules_dict.get(rule[0]).append(rule[1])
    else:
        rules_dict[rule[0]] = [rule[1]]

total = 0
for line in data:
    valid = True
    numbers = line.split(",")
    for i in range(1, len(numbers)):
        rule = rules_dict.get(numbers[i])
        for j in range(i):
            if rule != None and numbers[j] in rule:
              valid = False
    if valid:
        middle = int(numbers[len(numbers) // 2])
        total += middle

print(total)