q = int(input())
answers = []

for no in range(q):
    s = input().split(" ")
    x = int(s[0])
    y = int(s[1])
    z = int(s[2])

    if abs(x - z) < abs(y - z):
        answers.append("Cat A")
    elif abs(x - z) > abs(y - z):
        answers.append("Cat B")
    elif abs(x - z) == abs(y - z):
        answers.append("Mouse C")

for s in answers:
    print(s)
