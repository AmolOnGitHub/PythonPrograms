n = input()
s = input()

valley = 0
level = 0
valleyStart = False

for char in s:
    if char.upper() == "D":
        if level == 0:
            valleyStart = True    
        level -= 1

    else:         
        level += 1
        if level == 0 and valleyStart:
            valley += 1
            valleyStart = False

print(valley)
    