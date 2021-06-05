from itertools import combinations

def diff(uniList, a):
    if type(a) == int: return uniList.remove(a)
    for item in a:
        uniList.remove(item)
    return uniList

n, k = [int(x) for x in input().strip().split()]
s = [int(x) for x in input().strip().split()]
subsets = s.copy()

for x in range(2, n - 1):
    for comb in combinations(s, r = x):
        subsets.append(comb)

for subset in subsets[::-1]:
    comp = diff(s.copy(), subset)
    print(comp)
