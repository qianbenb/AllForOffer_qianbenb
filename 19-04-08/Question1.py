a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2],[3,4],[5,6],[7,8],[9,10]]
c = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

def printMatrix( matrix):
    # write code here
    row = len(matrix)
    collor = len(matrix[0])
    circle = (min(row, collor) - 1) // 2 + 1
    out_list = []
    if collor == 1:
        for i in range(row):
            out_list.append(matrix[i][0])
        return out_list
    print(circle)
    for j in range(circle):
        for i in range(j, collor - j):
            out_list.append(matrix[j][i])
        out_list.append('|')
        for i in range(j + 1, row - j):
            out_list.append(matrix[i][collor - j - 1])
        out_list.append('|')
        for i in range(collor - j - 2, j , -1):
            out_list.append(matrix[row - j - 1][i])
        out_list.append('|')
        for i in range(row - j - 1, j, -1):
            out_list.append(matrix[i][j])
        out_list.append('|')
    return out_list

print(printMatrix(c))