def getMatrix():
    row = int(input("Entger Number of row in matrix : "))
    column = int(input("Enter number of column  in matrix : "))
    martix = [[0, 0], [0, 0]]
    for m in range(row):
        for n in range(column):
            martix[m][n] = int(input("Enter the element in the matrix : "))
    return martix

def printMatrix(mat, row, column):
    matstr = ""
    for m in range(row):
        for n in range(column):
            matstr += str(mat[m][n])
            print(matstr)
        print("\n")
            
printMatrix(getMatrix(), 2, 2)
