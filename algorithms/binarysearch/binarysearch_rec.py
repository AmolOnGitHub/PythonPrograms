import math as math

def middle(begin, end):
    return math.floor((begin + end) / 2)

def binary(arr, toSearch, s, e, c):
    if c >= len(arr):
        mid = -1        
        return -1

    mid = middle(s, e) 
    if toSearch == int(arr[mid]):
        return mid
    elif toSearch < int(arr[mid]):
        return binary(arr, toSearch, s, mid, c + 1)
    elif toSearch > int(arr[mid]):
        return binary(arr, toSearch, mid + 1, e, c + 1)


arr = input().split(", ")
toSearch = int(input())
length = len(arr)

index = binary(arr, toSearch, 0, length - 1, 0)
print(toSearch, "is at index:", index)