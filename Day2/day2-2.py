item = []

with open("./Day2/input.txt", "r") as items:
    for i in items.readlines():
        item.append(i.split())

horizontal_position = 0
depth = 0
aim = 0

for i in range(len(item)):
    key = item[i][0]; value = item[i][1]
    if key == "forward":
        horizontal_position += int(value)
        depth += int(value) * aim
    elif key == "down": aim += int(value)
    elif key == "up": aim -= int(value)

print(horizontal_position * depth)
