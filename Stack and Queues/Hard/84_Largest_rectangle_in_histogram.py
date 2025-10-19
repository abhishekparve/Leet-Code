class Solution:
    # TC = 2 * (O(n) + O(n)) + O(n) = O(5n) --> 2 because nextSmaller and previousSmaller methods has the same code
    # SC = O(2n) + O(n) = O(4n)
    # Brute Force Solution
    def previousSmallerElement(self, heights):
        n = len(heights)
        stack = []
        res = [-1] * n
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(i)
        return res

    def nextSmallerElement(self, heights):
        n = len(heights)
        stack = []
        res = [n] * n
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                stack.pop()
            res[i] = stack[-1] if stack else n
            stack.append(i)
        return res

    def largestRectangleArea(self, heights):
        NSE = self.nextSmallerElement(heights)
        PSE = self.previousSmallerElement(heights)
        maxArea = 0
        for i in range(len(heights)):
            area = heights[i] * (NSE[i] - PSE[i] - 1)
            maxArea = max(maxArea, area)
        return maxArea

    # TC = O(n) + O(n)(for poping elements in stack) --> O(2n)
    # SC = O(n)
    def largestRectangleAreaOptimal(self, heights):
        stack = []
        n = len(heights)
        maxArea = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                elem = stack.pop()
                NSE = i
                PSE = stack[-1] if stack else -1
                area = heights[elem] * (NSE - PSE - 1)
                maxArea = max(area, maxArea)
            stack.append(i)

        while stack:
            elem = stack.pop()
            NSE = n
            PSE = stack[-1] if stack else -1
            area = heights[elem] * (NSE - PSE - 1)
            maxArea = max(maxArea, area)
        return maxArea


answer = Solution()
heights = [2, 1, 5, 6, 2, 3]
print(answer.largestRectangleArea(heights))
print(answer.largestRectangleAreaOptimal(heights))
