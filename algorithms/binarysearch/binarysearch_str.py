import math as math

def middle(begin, end):
    return math.floor((begin + end) / 2)

arr = input().split(", ")
toSearch = input()
length = len(arr) - 1

s = 0
e = length
mid = 0
c = 0
while not (arr[mid] == toSearch):
    if c >= length:
        mid = -1        
        break
    
    mid = middle(s, e)
    if arr[mid] > toSearch:
        e = mid - 1
    elif arr[mid] < toSearch:
        s = mid + 1
    c += 1

print(toSearch, "is at index:", mid)
if mid == -1:
    print("The element", toSearch, "is not present in the list of elements provided.")