from collections import Counter

n = input()
a = sorted(list(map(int, input().split(' '))))

x = Counter(a)
best = 0

for i in range(99):
    if i in a:
        best = max(x[i] + x[i + 1], best)

print(best)