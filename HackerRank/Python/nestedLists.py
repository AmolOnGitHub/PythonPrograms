def sortKey(item):
    return item[1]

n = int(input())
records = []

for _ in range(n):
    name = input()
    grade = float(input())
    records.append([name, grade])

records.sort(key = sortKey)
names = []
mark = records[0][1]

for i in records:
    if i[1] == records[0][1]:
        continue
    elif mark == records[0][1]:
        mark = i[1]
    if i[1] == mark:
        names.append(i[0])

names.sort()
for i in names:
    print(i)
