matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
spiralMatrix = []

left = 0
right = len(matrix[0]) - 1
top = 0
bottom = len(matrix) - 1

while left <= right and top <= bottom:
    for i in range(left, right + 1):
        spiralMatrix.append(matrix[top][i])
    top = top + 1

    for i in range(top, bottom + 1):
        spiralMatrix.append(matrix[i][right])
    right = right - 1
    if top <= bottom:
        for i in range(right, left - 1, -1):
            spiralMatrix.append(matrix[bottom][i])
        bottom = bottom - 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            spiralMatrix.append(matrix[i][left])
        left = left + 1

print(spiralMatrix)
