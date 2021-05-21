h = [int(x) for x in input().strip().split()]
word = input().lower()
mx = 0
for x in word:
    index = ord(x) - 97
    mx = max(mx, h[index])

print(mx * len(word))