a = 1
b = 2

sum = 0
i = 0
while a < 4000000 and b < 4000000:
    if a % 2 == 0:
        sum += a
    elif b % 2 == 0:
        sum += b
    
    if i % 2 == 0:
        a += b
    else:
        b += a
    
    i += 1


print(sum)