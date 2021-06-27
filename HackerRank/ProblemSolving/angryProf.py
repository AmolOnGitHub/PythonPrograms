t = int(input())

outputs = []

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    c = 0
    for x in a:
        if x <= 0: c += 1
        if c >= k: break
    if c >= k: outputs.append("NO")
    else: outputs.append("YES")

for output in outputs: print(output)
