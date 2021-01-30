# Multiples of 3 and 5

t = int(input())
sums = []
for i in range(t):
    n = int(input())
    sum = 0
    for j in range(n):
        if j % 3 == 0 or j % 5 == 0:
            sum += j
    sums.append(sum)

for i in sums:
    print(i)