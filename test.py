def ma(x):
    return x * x / (2 * x - 1)

x = 2
#while ma(x) != int(ma(x)):
for x in range(2, 100):
    print(ma(x))
    x += 1
