# https://leetcode.com/problems/word-search/description/


class Solution:
    def exists(self, board, word):
        direction = [(-1, 0), (0, 1), (0, -1), (1, 0)]

        def find(r, c, index):
            if index == len(word):
                return True
            if r < 0 or c < 0 or r >= row or c >= col or board[r][c] == "$":
                return False
            if board[r][c] != word[index]:
                return False
            temp = board[r][c]
            board[r][c] = "$"
            for dir in direction:
                new_r = r + dir[0]
                new_c = c + dir[1]
                if find(new_r, new_c, index + 1):
                    return True
            board[r][c] = temp
            return False

        row = len(board)
        col = len(board[0])
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and find(r, c, 0):
                    return True
        return False


answer = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(answer.exists(board, word))
