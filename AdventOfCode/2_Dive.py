with open("AdventOfCode/input_2.txt", "r") as f:
    direct = [x.strip() for x in f.readlines()]

h = 0
d = 0
aim = 0

for line in direct:
    x = int(line[-1])
    if "forward" in line:
        h += x
        d += aim * x
    if "down" in line:
        aim += x
    if "up" in line:
        aim -= x

print(h)
print(d)
print(h * d)