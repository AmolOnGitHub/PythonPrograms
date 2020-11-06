import math as m

ori = input().strip()
n = int(input())
repeatval = m.floor(n / len(ori))
rest = n % len(ori)

a_ori = ori.count("a")
a_new = a_ori * repeatval

counter = 1
for c in ori:
    if(counter >  rest): break
    elif(c == 'a'): a_new += 1
    counter += 1
    
print(a_new)
