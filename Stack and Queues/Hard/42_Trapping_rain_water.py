class Solution:
    # TC = O(3n) and SC = O(2n)
    def trapBrute(self, height):
        if not height:
            return 0
        n = len(height)
        total = 0
        leftMaxHeight = [0] * n
        rightMaxHeight = [0] * n
        leftMaxHeight[0] = height[0]
        rightMaxHeight[n - 1] = height[n - 1]
        # Calucating the left max height at each index
        for i in range(1, n):
            leftMaxHeight[i] = max(leftMaxHeight[i - 1], height[i])
        # Calucating the right max height at each index
        for j in range(n - 2, -1, -1):
            rightMaxHeight[j] = max(rightMaxHeight[j + 1], height[j])
        # Calculating the trapped water
        for i in range(len(height)):
            total += min(leftMaxHeight[i], rightMaxHeight[i]) - height[i]

        return total

    # Two pointer Solution
    # TC = O(n) SC = O(1)
    def trapOptimal(self, height):
        if not height:
            return 0
        n = len(height)
        leftMax = height[0]
        rightMax = height[n - 1]
        l = 0
        r = n - 1
        total = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                total += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                total += rightMax - height[r]
        return total


answer = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(answer.trapBrute(height))
print(answer.trapOptimal(height))
