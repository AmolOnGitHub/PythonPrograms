n, k, q = [int(x) for x in input().strip().split()]
a = [int(x) for x in input().strip().split()]
queries = [int(input()) for _ in range(q)]

temp = []
for x in range(n):
    ind = (x - k) % n
    temp.append(a[ind])

for query in queries:
    print(temp[query])
        