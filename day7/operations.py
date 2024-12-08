totals = []
components = []

with open("data.txt","r") as file:
    for line in file.readlines():
        stripped_line = line.strip()
        split_line = stripped_line.split(":")
        totals.append(int(split_line[0]))
        comps = []
        for item in split_line[1].strip().split(" "):
            comps.append(int(item))
        components.append(comps)

class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

def add_nodes(parent, list):
    if len(list) > 0:
        parent.left = Node(parent.data + list[0])
        parent.right = Node(parent.data * list[0])
        add_nodes(parent.left, list[1:])
        add_nodes(parent.right, list[1:])

def search(node, number):
    if (node.left == None and node.right == None):
        if (node.data == number):
            return True
        else:
            return False
    return (search(node.left, number) or search(node.right, number))

output = 0
i = 0
for entry_list in components:
    root = Node(entry_list[0])
    add_nodes(root, entry_list[1:])
    if search(root, totals[i]) == True:
        output += totals[i]
    i += 1
    
print(output)