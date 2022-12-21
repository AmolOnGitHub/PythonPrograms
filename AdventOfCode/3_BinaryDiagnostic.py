def most_common(arr):
    arr.sort()
    mc = arr[0]
    last = ""
    for x in arr:
        if x == last: continue
        if arr.count(x) > arr.count(mc):
            mc = x
        last = x
    
    return mc

def least_common(arr):
    arr.sort()
    lc = arr[0]
    last = ""
    for x in arr:
        if x == last: continue
        if arr.count(x) < arr.count(lc):
            lc = x
        last = x
    
    return lc

def toDec(snum):
    dec = 0
    for i in range(len(snum)):
        if snum[i] == "1":
            dec += pow(2, len(snum) - i - 1)
        
    return dec

with open("AdventOfCode/input_3.txt", "r") as f:
    bn = [x.strip() for x in f.readlines()]

gamma = ""
epsilon = ""

for i in range(len(bn[0])):
    x = []
    for j in range(len(bn)):
        x.append(bn[j][i])
    gamma += most_common(x)
    epsilon += least_common(x)

print(toDec(gamma))
print(toDec(epsilon))
print(toDec(gamma) * toDec(epsilon))