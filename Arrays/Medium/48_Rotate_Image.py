# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# The time complexity of this solution is O(n^2), where n is the size of the matrix.
# This is because we iterate through each element in the matrix once in the nested for loop.

# The space complexity is O(1) because we are modifying the matrix in-place 
# without using any additional space that scales with the input size.

class Solution:
    def rotateImage(self, matrix):
        l = 0
        r = len(matrix) - 1
        while l < r:
            for i in range(r - l):
                Top = l
                Bottom = r
                # save matix top left value to topLeft variable
                topLeft = matrix[Top][l + i]
                # move matix bootom left to matrix top left
                matrix[Top][l + i] = matrix[Bottom - i][l]
                # move matix bootom right to matrix bottom left
                matrix[Bottom - i][l] = matrix[Bottom][r - i]
                # move matrix top right to matrix bottom right
                matrix[Bottom][r - i] = matrix[Top + i][r]
                # move the value of top left to matrix top right
                matrix[Top + i][r] = topLeft
            l += 1
            r -= 1
        print(matrix)

answer = Solution()
answer.rotateImage([[1,2,3],[4,5,6],[7,8,9]])