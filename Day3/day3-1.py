item = []

with open("./Day3/input.txt", "r") as items:
    for i in items.readlines():
        item.append(i.split())

dashed = []
for i in item:
    for j in i: dashed.append(j)

valid = ['' for i in range(len(dashed[0]))]
for i in range(len(dashed)):
    m = dashed[i]
    for j in range(len(m)):
        valid[j] += m[j]

most_bit = ''
least_bit = ''

for thing in valid:
    count = 0
    for j in thing:
        if j == '0': count += 1

    zth = count; oth = len(thing) - zth
    if zth > oth:
        most_bit += '0'; least_bit += '1'
    else:
        most_bit += '1'; least_bit += '0'

print(int(most_bit, 2) * int(least_bit, 2))
