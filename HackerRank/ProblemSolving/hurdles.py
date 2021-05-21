n, k = [int(x) for x in input().strip().split()]
height = [int(x) for x in input().strip().split()]
height.sort()

if k >= height[-1]:
    print(0)
else: print(height[-1] - k)