
k = int(input())
cases = [input() for _ in range(k)]
for s in cases:
    if s.isnumeric():
        pass
    elif not s.isnumeric():
        print(s[::2], s[1::2])
        k += 1

