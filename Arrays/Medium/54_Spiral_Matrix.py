# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# The time complexity of this solution is O(m*n), where m is the number of rows in the matrix 
# and n is the number of columns. This is because we iterate through each element in the matrix exactly once.

# The space complexity is O(1) because we are not using any additional space that grows with the input size.
# The result list is the only additional space used, but its size is fixed and does not depend on the input size.

class Solution:
    def spriralMatrix(self, matrix):
        result = []
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        while left < right and top < bottom:
            # for every i from left to right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            # for every i from top to bottom
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            if not(left < right and top < bottom):
                break
            # for every i from right to left
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1
            # for every i from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        return print(result)
    
answer = Solution()
answer.spriralMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
