def fac(x):
    if x == 2 or x == 1:
        return x
    if x == 0: 
        return 1
    return x * fac(x - 1)

print(fac(int(input())))