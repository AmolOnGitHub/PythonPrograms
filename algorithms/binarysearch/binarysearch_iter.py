import math as math

def middle(begin, end):
    return math.floor((begin + end) / 2)

arr = input().split(", ")
toSearch = int(input())
length = len(arr) - 1

s = 0
e = length
mid = 0

while not (int(arr[mid]) == toSearch):
    mid = middle(s, e)
    if int(arr[mid]) > toSearch:
        e = mid
    elif int(arr[mid]) < toSearch:
        s = mid + 1

print(toSearch, "is at index:", mid)
