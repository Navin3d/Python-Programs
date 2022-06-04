a = [[2, 3], [7, 9]]
b = [[4, 11], [90, 92]]
c = [[0, 0], [0, 0]]

for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            c [i][j] += a[i][k] * b[k][j]
print(c)
