# https://leetcode.com/problems/find-a-peak-element-ii/


class Solution:
    # TC : O(m log(n))
    # where m is row and n is col
    def findRowIndex(self, mat, row, col):
        maxElem = -1
        index = -1
        for i in range(row):
            if mat[i][col] > maxElem:
                maxElem = mat[i][col]
                index = i
        return index

    def findPeakElement2(self, mat):
        row = len(mat)
        col = len(mat[0])
        l = 0
        r = col - 1
        while l <= r:
            mid = l + (r - l) // 2
            rowIndex = self.findRowIndex(mat, row, mid)
            left = mat[rowIndex][mid - 1] if mid - 1 >= 0 else -1
            right = mat[rowIndex][mid + 1] if mid + 1 >= 0 else -1
            if mat[rowIndex][mid] > left and mat[rowIndex][mid] > right:
                return [rowIndex, mid]
            elif mat[rowIndex][mid] < left:
                r = mid - 1
            else:
                l = mid + 1
        return [-1, -1]


answer = Solution()
mat = [[10, 20, 15], [21, 30, 14], [7, 16, 32]]
print(answer.findPeakElement2(mat))
