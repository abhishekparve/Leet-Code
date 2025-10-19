# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# The time complexity of this solution is O(1) because the size of the board is fixed at 9x9,
# so the number of iterations in the nested loops is constant.

# The space complexity is also O(1) because the size of the collections.defaultdict objects (col, row, square) is also fixed at 9x9.

import collections
class Solution:
    def validSudoku(self, board):
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        square = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[r//3, c//3]:
                    return print("False")
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[r//3, c//3].add(board[r][c])
        return print("True")
    
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

answer = Solution()
answer.validSudoku(board)
