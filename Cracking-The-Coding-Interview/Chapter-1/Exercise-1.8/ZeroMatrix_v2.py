def ZeroMatrix(matrix):
    rows = []
    columns = []
    n = len(matrix[0])

    for i in range(n):
        rows.append(False)
        columns.append(False)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = True
                columns[i] = True
            
    for i in range(n):
        for j in range(n):
            if rows[i] or columns[j]:
                matrix[i][j] = 0

    return matrix

print(ZeroMatrix([[1,2,3],[4,5,6],[7,8,9]]))
print(ZeroMatrix([[1,2,3],[4,0,6],[7,8,9]]))
print(ZeroMatrix([[0,2,3],[4,5,6],[7,8,9]]))