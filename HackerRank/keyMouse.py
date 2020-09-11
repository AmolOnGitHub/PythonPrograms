import sys

def add(n, sarray):
    new = []
    i = 0
    while i < n:
        new.append(int(sarray[i]))
        i += 1
    return new

keyboards = []
drives = []
b = 0

s1 = input().split(" ")
skey = input().split(" ")
sdrive = input().split(" ")

b = int(s1[0])
n = int(s1[1])
m = int(s1[2])

keyboards = add(n, skey)
drives = add(m, sdrive)

keyboards.sort()
drives.sort()

if keyboards[0] + drives[0] > b:
    print("-1")
    sys.exit()

totals = []
for x in keyboards:
    for y in drives:
        totals.append(x + y)

highest = 0
for x in totals:
    if x > highest and x <= b:
        highest = x

print(highest)

