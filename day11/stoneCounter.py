data = []

with open("data.txt", "r") as file:
    split_string = file.read().strip().split(" ")
    data = [int(x) for x in split_string]

def blink():
    i = 0
    limit = len(data)
    while i < limit:
        if data[i] == 0:
            data[i] = 1
        elif len(str(data[i])) % 2 == 0:
            num_string = str(data[i])
            left = num_string[:len(num_string) // 2]
            right = num_string[len(num_string) // 2:]
            data[i] = int(left)
            data.insert(i + 1, int(right))
            i += 1
            limit += 1
        else:
            data[i] = data[i] * 2024
        i += 1

for i in range(25):
    blink()
    print(i, len(data))
