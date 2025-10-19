# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1
 
# The time complexity of this solution is O(n), where n is the length of the input list height.
# This is because we are using a two-pointer approach to iterate through the list once,
# comparing the heights at each position and calculating the area. The while loop will run at most n times.

# The space complexity of this solution is O(1) because we are not using any additional data structures that grow with the input size.
# We only need a constant amount of space to store the variables max_area, l, and r.

class Solution:
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) *min(height[left], height[right])
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return print(max_area)
    
answer = Solution()
answer.maxArea([1,8,6,2,5,4,8,3,7])