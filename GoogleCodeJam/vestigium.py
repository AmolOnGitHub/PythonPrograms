def convertInt(arr):
    length = len(arr)
    for i in range(length):
        arr[i] = int(arr[i])
    return arr

def getInput(testcases):
    matrices = []
    n = []

    for i in range(testcases):
        n.append(int(input()))
        testcurrent = []
        j = 0
        while j < n[i]:
            arrcur = input().split(" ")
            arrcur = convertInt(arrcur)
            testcurrent.append(arrcur)
            j += 1
        matrices.append(testcurrent)
    return matrices

def calculate(testcases, matrices):
    for i in range(testcases):
        testcaseno = i + 1
        n = len(matrices[i][0])

        # Finding Diagonal Sum
        diagonalsum = 0
        for j in range(n):
            diagonalsum += matrices[i][j][j]

        # Find no. of rows which contain repeated elements
        rowrepeat = 0
        for j in range(n):
            temp = matrices[i][j]
            temp = sorted(temp)
            k = 0
            while k < len(temp) - 1:
                if temp[k] == temp[k + 1]:
                    rowrepeat += 1
                    break
                k += 1

        # Find no. of columns which contain repeated elements
        colrepeat = 0
        for j in range(n):
            temp = []
            for k in range(n):
                temp.append(matrices[i][k][j])
            temp = sorted(temp)
            k = 0
            while k < len(temp) - 1:
                if temp[k] == temp[k + 1]:
                    colrepeat += 1
                    break
                k += 1

        print("Case #" + str(testcaseno) + ":", diagonalsum, rowrepeat, colrepeat)

    
testcases = int(input())
matrices = getInput(testcases)
calculate(testcases, matrices)