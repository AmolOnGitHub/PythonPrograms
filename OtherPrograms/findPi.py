import random

def avg(arr):
    sum = 0
    for no in arr:
        sum += no
    return sum/len(arr)

def findpi(n):
    inside = 0
    i = 1
    while i <= n:
        r = random.random() ** 2 + random.random() ** 2
        if r < 1: 
            inside += 1    
        i += 1
    return 4 * inside / n

i = 1
pival = []
while i > 0:
    pival.append(findpi(100000))
    i -= 1

print(avg(pival))

