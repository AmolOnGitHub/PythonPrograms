def swap(l):
    c = 0
    while c < len(l):
        l[c] = abs(l[c] - 1)
        c += 1
    return l

l = [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]

for x in l:
    if x == 1:
        l = swap(l)

print(l.count(0))
