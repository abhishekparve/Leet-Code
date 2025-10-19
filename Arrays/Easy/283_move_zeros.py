# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Method 1 : TC: O(n) SC: O(1)
class Solution:
    def moveZeros(self, nums):
        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        while(index < len(nums)):
            nums[index] = 0
            index += 1
        return(print(nums))

answer = Solution()
answer.moveZeros([0, 0, 1])

# Method 2 : Two pointers, TC: O(n) SC: O(1)
class Solution2:
    def moveZeros(self, nums):
        index = 0
        for n in range(len(nums)):
            if nums[n] != 0:
                # If the current element is non-zero, swap it with the element at index
                # This effectively moves non-zero elements to the beginning of the list
                nums[n], nums[index] = nums[index], nums[n]
                index += 1
        return print(nums)

# answer2 = Solution()
# answer2.moveZeros([0, 0, 1])