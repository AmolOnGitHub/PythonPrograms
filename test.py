arr = [1, 2, 3, 4, 5, 6]
k = 3
n = len(arr)

temp = []
for x in range(n):
    ind = (x - k) % n
    temp.append(arr[ind])

print(temp)