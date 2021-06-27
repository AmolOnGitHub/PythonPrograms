t = int(input())
n = [int(input()) for _ in range(t)]

for cycle in n:
    height = 0
    for x in range(int((cycle + 1) / 2)):
        height = 2 * (height + 1)
    if cycle % 2 == 0: height += 1
    print(height)
