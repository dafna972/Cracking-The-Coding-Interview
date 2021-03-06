def RotateMatrix(matrix):
    n = len(matrix[0]) - 1
    for i in range(n):
        for j in range(i,n-i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-j][i]
            matrix[n-j][i] = matrix[n-i][n-j]
            matrix[n-i][n-j] = matrix[j][n-i]
            matrix[j][n-i] = temp
    return matrix

print(RotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))
print([[7,4,1],[8,5,2],[9,6,3]])
print(RotateMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
print([[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]])