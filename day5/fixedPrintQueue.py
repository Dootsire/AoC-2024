queueText = []

with open("data.txt", "r") as file:
    for line in file.readlines():
        queueText.append(line.strip())

rule_data_split = queueText.index('')
data = queueText[rule_data_split + 1:]
rules = queueText[:rule_data_split]
rules_dict = {}

for line in rules:
    rule = line.split("|")
    if rule[0] in rules_dict:
        rules_dict.get(rule[0]).append(rule[1])
    else:
        rules_dict[rule[0]] = [rule[1]]

def needs_fixing(numbers, rules_dict):
    for i in range(1, len(numbers)):
        rule = rules_dict.get(numbers[i])
        for j in range(i):
            if rule != None and numbers[j] in rule:
              return True
    return False

to_fix = []

for i in range(len(data)):
    numbers = data[i].split(",")
    if needs_fixing(numbers, rules_dict):
        to_fix.append(numbers)

def fixed(numbers, rules_dict):
    output = numbers
    for x in range(len(numbers)):
        for i in range(len(numbers)):
            rule = rules_dict.get(numbers[i])
            for j in range(i):
                if rule != None and numbers[j] in rule:
                    tmp = output[i]
                    output[i] = output[i-1]
                    output[i-1] = tmp
    return output

total = 0

for numbers in to_fix:
    fixed_line = fixed(numbers, rules_dict)
    total += int(fixed_line[len(fixed_line)//2])
print(total)