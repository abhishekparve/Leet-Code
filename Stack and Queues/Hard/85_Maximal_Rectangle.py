# https://leetcode.com/problems/maximal-rectangle/description/


# TC = O(m * n) SC = O(2n)
class Solution:
    def findMaxArea(self, height):
        maxArea = 0
        stack = []
        n = len(height)
        for i in range(n):
            while stack and height[stack[-1]] > height[i]:
                elem = stack.pop()
                NSE = i
                PSE = stack[-1] if stack else -1
                area = height[elem] * (NSE - PSE - 1)
                maxArea = max(area, maxArea)
            stack.append(i)
        while stack:
            elem = stack.pop()
            NSE = n
            PSE = stack[-1] if stack else -1
            area = height[elem] * (NSE - PSE - 1)
            maxArea = max(area, maxArea)
        return maxArea

    def maximalRectangle(self, matrix):
        col = len(matrix[0])
        row = len(matrix)
        maxArea = 0
        height = [0] * col
        # Calcuating the max area of the first row by passing it is 1 D array
        # in findMax method

        for i in range(col):
            height[i] = 1 if matrix[0][i] == "1" else 0

        maxArea = max(maxArea, self.findMaxArea(height))

        # Calculating the area for the rest of the rows
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == "0":
                    height[c] = 0
                else:
                    height[c] += 1
            maxArea = max(maxArea, self.findMaxArea(height))
        return maxArea


answer = Solution()
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(answer.maximalRectangle(matrix))
