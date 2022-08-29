item = []

with open("./Day1/input.txt", "r") as items:
    for i in items.readlines():
        for j in i.split(): item.append(int(j))

count = 0
last = sum(item)

for i in range(len(item)):
    sm = 0
    if i + 3 <= len(item):
        for j in range(i, i + 3):
            sm += item[j]
    if (last < sm): count += 1
    last = sm

print(count)
