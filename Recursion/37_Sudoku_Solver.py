class Solution:
    def sudokuSolver(self, board):
        row = len(board)
        col = len(board[0])

        def isValid(r, c, ch):
            for i in range(9):
                if board[i][c] == ch:
                    return False
                if board[r][i] == ch:
                    return False
                if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == ch:
                    return False
            return True

        def solve():
            for r in range(row):
                for c in range(col):
                    if board[r][c] == ".":
                        for ch in "123456789":
                            if isValid(r, c, ch):
                                board[r][c] = ch
                                if solve():
                                    return True
                                board[r][c] = "."
                        return False
            return True

        solve()
        return board


answer = Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(answer.sudokuSolver(board))
