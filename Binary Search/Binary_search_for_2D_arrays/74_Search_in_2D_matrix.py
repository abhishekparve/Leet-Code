# https://leetcode.com/problems/search-a-2d-matrix/description/


class Solution:
    # O(n * m)
    def searchMatrixBrute(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == target:
                    return print("True")
        return print("False")

    # O(m + n)
    def searchMatrixBetter(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n - 1
        while i < m and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return print("True")
        return print("False")

    # O(log(n * m))
    def searchMatrixOptimal(self, matrix, target):
        r = len(matrix)
        c = len(matrix[0])

        start = 0
        end = (r * c) - 1
        while start <= end:
            mid = start + (end - start) // 2
            # lets assume if you get the mid = 8 and column is 3
            # then the corresponding cell in the 2-D matric will be
            # row = 8//3 = 2
            # col = 8 % 3 = 2
            # in matrix the cell will be matrix[2][2]
            row = mid // c
            col = mid % c
            if matrix[row][col] > target:
                end = mid - 1
            elif matrix[row][col] < target:
                start = mid + 1
            else:
                return print("True")
        return print("False")


answer = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 10
# answer.searchMatrixOptimal(matrix, target)
# answer.searchMatrixBrute(matrix, target)
answer.searchMatrixBetter(matrix, target)
