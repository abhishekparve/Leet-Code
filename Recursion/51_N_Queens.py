# https://leetcode.com/problems/n-queens/description/


class Solution:
    def solveNQueen(self, n):
        result = []
        board = [["."] * n for i in range(n)]

        def isValid(r, c):
            for i in range(n):
                # Check in the same column at each row
                if board[i][c] == "Q":
                    return False
                # Check right side diagonally
                # If right then decrement r and increment c
                if r - i >= 0 and c + i < n and board[r - i][c + i] == "Q":
                    return False
                # Check left side diagonally
                # if left then decrement r and decrement c
                if r - i >= 0 and c - i >= 0 and board[r - i][c - i] == "Q":
                    return False
            return True

        def backtrack(r):
            # base case
            # if row equals n then we exit
            # here we are creating another copy list so that we can aapend the copy
            # list to our result list. Because here we want to return each row in string format
            # and we want to avoid modifying the board list
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            # Iterating over each colum in the board and trying to place
            # the queen based on the valid position in each row
            for c in range(n):
                if isValid(r, c):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."

        backtrack(0)
        return result

    def solveNQueenApproach2(self, n):
        result = []
        col = set()
        posDiag = set()  # r + c
        negDiag = set()  # r - c
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            for c in range(n):
                if c in col or r + c in posDiag or r - c in negDiag:
                    continue
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return result


answer = Solution()
n = 4
# print(answer.solveNQueen(n))
print(answer.solveNQueenApproach2(n))
