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

def selection(arr, begin, end):
    if begin == end:
        return arr

    minIndex = findMinIndex(arr, begin, end)
    
    temp = arr[minIndex]
    arr[minIndex] = arr[begin]
    arr[begin] = temp

    return selection(arr, begin + 1, end)

arr = input().split(", ")

print(selection(arr, 0, len(arr) - 1))


    