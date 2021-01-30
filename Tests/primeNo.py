n = int(input())
primes = []
x = 2

while x <= n:
    isDiv = False
    for prime in primes:
        if x % prime == 0:
            isDiv = True
            break
        elif prime * prime > x:
            break
    if not isDiv:
        primes.append(x)
        
    if x >= 3: x += 2
    else: x += 1    

print(primes)