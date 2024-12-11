from functools import cache

data = []

with open("data.txt", "r") as file:
    split_string = file.read().strip().split(" ")
    data = [int(x) for x in split_string]

max = 75

@cache
def blink_int(number, iteration):
    if (iteration == max):
        return 1
    next_it = iteration + 1

    if (number == 0):
        return blink_int(1, next_it)
    
    string_length = len(str(number))
    if string_length % 2 == 0:
        num_string = str(number)
        left = num_string[:len(num_string) // 2]
        right = num_string[len(num_string) // 2:]
        return blink_int(int(left), next_it) + blink_int(int(right), next_it)

    return blink_int(number * 2024, next_it)

output = 0
for num in data:
    output += blink_int(num, 0)
print(output)