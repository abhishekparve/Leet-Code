# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

# The time complexity of the solution is O(log n)
# because it uses binary search to find the left and right positions of the target element in the given array.
# In each iteration of the binary search, the search space is divided in half, resulting in a logarithmic time complexity.

# The space complexity of the solution is O(1) 
# because it uses a constant amount of extra space to store the left and right positions of the target element.

class Solution():
    def position(self, nums, target):
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return print([left, right])
        
        
    def binarySearch(self, nums, target, leftBias):
        l = 0
        r = len(nums) - 1
        i = -1
        while l <= r:
            mid = (l + r) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                i = mid
                if leftBias:
                    r = mid - 1
                else:
                    l = mid + 1
        return i
    
answer = Solution()
answer.position([5,7,7,8,8,10], 8)
answer.position([], 8)


