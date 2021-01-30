n = int(input())
arr = list(map(int, input().strip().split(" ")))
arr.sort(reverse = True)

counter = 0
at = arr[0]
while arr[counter] >= at:
    counter += 1

print(arr[counter])