item = []

with open("./Day1/input.txt", "r") as items:
    for i in items.readlines():
        for j in i.split(): item.append(int(j))

count = 0

for i in range(len(item)):
    if (i - 1) >= 0:
        if item[i - 1] < item[i]: count += 1

print(count)
