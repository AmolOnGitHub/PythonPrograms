no = int(input())
arr = [int(input()) for i in range(no)]
numbers = []

for k in arr:
    if(numbers.count(k) == 0): #number has not been seen before
        numbers.append(k)

countNo = [arr.count(m) for m in numbers]
highest = 0
highestIndex = 0
counter = 0

while counter < len(countNo) - 1:
    current = countNo[counter]
    if(current > highest):
        highest = current
        highestIndex = counter
    counter += 1

print("Mode is", numbers[highestIndex])
