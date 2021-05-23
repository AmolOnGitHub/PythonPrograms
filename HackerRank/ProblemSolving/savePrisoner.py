t = int(input())

tot = []
for x in range(t):
    tot.append([int(x) for x in input().strip().split()])

for x in tot:
    n, m, s = x
    last = ((m % n) + s - 1) % n
    if last == 0: print(n)
    else: print(last)