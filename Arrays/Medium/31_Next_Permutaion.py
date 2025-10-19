# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]

# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]
 
# The time complexity of this solution is O(n), where n is the length of the input list nums.
# This is because we iterate through the list once to find the pointer position,
# and then iterate through the remaining elements to find the next greater element to swap with the pointer element. 
# Reversing the sublist after the pointer position also takes O(n) time. Therefore, the overall time complexity is O(n).

# The space complexity of this solution is O(1) because we are not using any additional data structures that grow with the input size.
# We are only using a constant amount of extra space to store the pointer variable. Therefore, the space complexity is O(1).

class Solution:
    def nextPermutation(self, nums):
        length = len(nums)
        pointer = length - 2
        # Base case
        if length <= 2:
            return nums.reverse()
        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -= 1
        if pointer == -1:
            return nums.reverse()
        for x in range(length - 1, pointer, -1):
            if nums[pointer] < nums[x]:
                nums[pointer], nums[x] = nums[x], nums[pointer]
                break
        nums[pointer + 1:] = reversed(nums[pointer + 1:])
        print(nums)
    
answer = Solution()
answer.nextPermutation([1,2,3])
