matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

# My Brutforce Approach takes more space and time
# def setZeroes(matrix):
#     zeroIndex = []

#     rows = len(matrix)
#     cols = len(matrix[0])

#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 0:
#                 zeroIndex.append((i, j))

#     for i, j in zeroIndex:
#         for col in range(cols):
#             matrix[i][col] = 0

#     for i, j in zeroIndex:
#         for row in range(rows):
#             matrix[row][j] = 0


# Approach 2 : Better
# def setZeroes(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])

#     rowMark = [False] * rows
#     colMark = [False] * cols

#     # Mark rows and columns
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 0:
#                 rowMark[i] = True
#                 colMark[j] = True

#     # Update matrix
#     for i in range(rows):
#         for j in range(cols):
#             if rowMark[i] or colMark[j]:
#                 matrix[i][j] = 0


# Approach 3: Optimal

# def setZeroes(self, matrix):
#         rows = len(matrix)
#         cols = len(matrix[0])

#         firstRowZero = False
#         firstColZero = False

#         # Check first row
#         for j in range(cols):
#             if matrix[0][j] == 0:
#                 firstRowZero = True

#         # Check first column
#         for i in range(rows):
#             if matrix[i][0] == 0:
#                 firstColZero = True

#         # Use first row and column as markers
#         for i in range(1, rows):
#             for j in range(1, cols):
#                 if matrix[i][j] == 0:
#                     matrix[i][0] = 0
#                     matrix[0][j] = 0

#         # Zero cells based on markers
#         for i in range(1, rows):
#             for j in range(1, cols):
#                 if matrix[i][0] == 0 or matrix[0][j] == 0:
#                     matrix[i][j] = 0

#         # Zero first row if needed
#         if firstRowZero:
#             for j in range(cols):
#                 matrix[0][j] = 0

#         # Zero first column if needed
#         if firstColZero:
#             for i in range(rows):
#                 matrix[i][0] = 0
