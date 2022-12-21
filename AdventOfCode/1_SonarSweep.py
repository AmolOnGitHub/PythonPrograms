with open("AdventOfCode/input_1", "r") as f:
    l = [int(x) for x in f.readlines()]

s = 0
slist = []
for i in range(0, len(l) - 2):
    slist.append(sum(l[i:i+3]))

c = 0
for i in range(0, len(slist) - 1):
    if slist[i] < slist[i + 1]:
        c += 1

print(c)