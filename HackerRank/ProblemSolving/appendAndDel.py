s = input()
t = input()
k = int(input())
counter = 0

while not t.startswith(s):
    s = s[:-1]
    counter += 1

counter += len(t) - len(s)

if counter < k:
    if (s == '' or s == t) and len(t) <= (k / 2):
        print("Yes")
    elif (k - counter) % 2 == 0:
            print("Yes")
    else: print("No")

elif counter == k: print("Yes")
else: print("No")   