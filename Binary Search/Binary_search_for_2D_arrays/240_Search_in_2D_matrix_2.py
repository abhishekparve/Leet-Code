class Solution:
    # O(n * m)
    def searchMatrix(self, matrix, target):
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == target:
                    return print("True")
        return print("False")

    def Binary(self, matrix, target):
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid] > target:
                r = mid - 1
            elif matrix[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1

    # O(n log(m)) where n = row and m = col
    def searchMatrixBinary(self, matrix, target):
        r = len(matrix)
        for i in range(r):
            result = self.Binary(matrix[i], target)
            if result > -1:
                return print("True")
        return print("False")

    # O(n + m)
    def searchMatrixOptimal(self, matrix, target):
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


answer = Solution()
matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
target = 5
# print(answer.searchMatrix(matrix, target))
# print(answer.searchMatrixBinary(matrix, target))
print(answer.searchMatrixOptimal(matrix, target))
