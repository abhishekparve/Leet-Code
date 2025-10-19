# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.

# Example 1:
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.

# Example 2:
# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct m

# The time complexity of this solution is O(n), where n is the number of elements in the input list.
# This is because we are using the set() function to remove duplicates from the list, which has a time complexity of O(n).
# Additionally, we are using the max() function three times, which also has a time complexity of O(n).
# Therefore, the overall time complexity is O(n).

# The space complexity of this solution is O(n), where n is the number of elements in the input list.
# This is because we are creating a set() to store the unique elements from the list,
# which requires additional space proportional to the number of elements in the list.
# Therefore, the overall space complexity is O(n).

class Solution:
    def thirdMax(self, nums):
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        else:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)
        
answer = Solution()
answer.thirdMax([1,2,3])