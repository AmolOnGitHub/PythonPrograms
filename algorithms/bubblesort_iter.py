arr = input().split(" ")
length = len(arr) - 1
switch = False

for i in range(length):
    for j in range(length - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            switch = True
    if not switch:
        break

print(arr)
