import math as math

def middle(begin, end):
    return math.floor((begin + end) / 2)

def binary(arr, toSearch, s, e):
    mid = middle(s, e) 
    if toSearch == int(arr[mid]):
        return mid
    elif toSearch < int(arr[mid]):
        return binary(arr, toSearch, s, mid)
    elif toSearch > int(arr[mid]):
        return binary(arr, toSearch, mid + 1, e)


arr = input().split(", ")
toSearch = int(input())
length = len(arr)

index = binary(arr, toSearch, 0, length - 1)
print(toSearch, "is at index:", index)