from collections import Counter

n = input()
a = sorted(list(map(int, input().split(' '))))
subA = []

while len(a) > 1:
    sub = []
    first = a[0]
    newIndex = 0
    popCounter = 0
    for no in a:
        if no == first:
            sub.append(no)
            popCounter += 1
        if no == first + 1:
            if newIndex == 0: newIndex = a.index(no)
            sub.append(no)
        if no > first + 1:
            break
        if len(a) == 1:
            break
    subA.append(sub)
    for _ in range(popCounter):
        a.pop(0)

maxLen = 0
for arr in subA:
    if len(arr) > maxLen:
        maxLen = len(arr)

print(maxLen)