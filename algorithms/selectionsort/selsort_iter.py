def findMinIndex(arr, begin, end):
    min = float('inf')
    i = begin
    index = end
    while i <= end:
        no = int(arr[i])
        if no < min:
            min = no
            index = i
        i += 1

    return index

arr = input().split(", ")
lengthIndex = len(arr) - 1
i = 0

while i <= lengthIndex:
    minIndex = findMinIndex(arr, i, lengthIndex)
    min = arr[minIndex]
    temp = arr[i]

    arr.pop(i)
    arr.insert(i, min)
    arr.pop(minIndex)
    arr.insert(minIndex, temp)

    i += 1

print(arr)

