def rev(x: int):
    rev = 0
    while x > 0:
        rev = rev * 10 + x % 10
        x //= 10
    return rev

i, j, k = [int(x) for x in input().split()]
c = 0

for day in range(i, j + 1):
    temp = day - rev(day)
    if temp % k == 0: c += 1

print(c)
