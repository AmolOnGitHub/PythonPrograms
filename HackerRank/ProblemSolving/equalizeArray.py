def findCount(arr):
    arr.sort()
    newarr = []
    length = len(arr)
    i = 0
    while i < length:
        no = arr[i]
        c = 0
        j = i
        while j < length:
            if arr[j] == no:
                c += 1
            elif not arr[j] == no:
                break 
            j += 1
        i += c
        toadd = str(no) + "-" + str(c)
        newarr.append(toadd)
    return(newarr)

def equalizeArray(arr):
    countArr = findCount(arr)
    lengthCount = len(countArr)

    # Now to find the max count of a number.
    maxCount = 0
    for i in range(lengthCount):
        s = countArr[i]
        splitCount = s.split("-")
        count = int(splitCount[1])
        
        if int(count) > int(maxCount):
            maxCount = count

    return len(arr) - maxCount

n = input()
arr = input().split(" ")
print(equalizeArray(arr))