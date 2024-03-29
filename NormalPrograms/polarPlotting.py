import matplotlib.pyplot as plt
import math

def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def toCart(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)

xP = []
yP = []

for i in range(10000):
    if not is_prime(i):
        continue
    x, y = toCart(i, i)
    xP.append(x)
    yP.append(y)

plt.plot(xP, yP, ".")
plt.show()
