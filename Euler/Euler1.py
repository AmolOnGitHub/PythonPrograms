t = int(input().strip())
n = []
for a0 in range(t):
    n.append(int(input().strip()))
    
for num in n:
    l = list(range(3, num, 3))
    l += list(range(5, num, 5))
    l = list(set(l))
    print(sum(l))