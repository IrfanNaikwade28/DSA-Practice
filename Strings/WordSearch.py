board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"


def findWord(board, i, j, word, idx, directions):
    if idx == len(word):
        return True

    if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or board[i][j] == "$":
        return False

    if board[i][j] != word[idx]:
        return False

    temp = board[i][j]
    board[i][j] = "$"  # marked to show visited

    for dr, dc in directions:
        if findWord(board, i + dr, j + dc, word, idx + 1, directions):
            board[i][j] = temp
            return True

    board[i][j] = temp
    return False


def WordSearch(board, word):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0] and findWord(board, i, j, word, 0, directions):
                    return True

    return False


print(WordSearch(board, word))
