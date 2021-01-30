def convert(inx):
    smol = []
    for n in inx:
        smol.append(n)
    return smol

def calc(mat):
    sums = []
    sum = 0

    for x in range(3):
        for y in range(3):
            sum += int(mat[x][y])
        sums.append(sum)
        sum = 0

    for x in range(3):
        for y in range(3):
            sum += int(mat[y][x])
        sums.append(sum)
        sum = 0

    for x in range(3):
        sum += int(mat[x][x])
    sums.append(sum)
    sum = 0

    sum = int(mat[0][2]) + int(mat[1][1]) + int(mat[2][0])
    sums.append(sum)
    return sums

in1 = input().split(" ")
in2 = input().split(" ")
in3 = input().split(" ")

mat = []
mat.append(convert(in1))
mat.append(convert(in2))
mat.append(convert(in3))

sums = calc(mat)

print(mat)
print(sums)

   
