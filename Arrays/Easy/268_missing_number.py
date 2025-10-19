# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
# 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2

# Method 1 : Time complexity = O(nlogn) because all the sorting function uses log n complexity and we are iterating through
#            the nums array n times so the time complexity O(nlogn)
#            Space complexity = O(1)
class Solution:
    def missingNumber(self, nums):
        nums = sorted(nums)
        i = 1
        for i in range(1, len(nums)):
            difference = nums[i] - nums[i-1]
            if not difference == 1:
                result = nums[i]
                result -= 1
            elif difference == 1:
                result = nums[i]
                result += 1
        return result
    
answer = Solution()
answer.missingNumber([0, 3, 1])

#Method 2 (Efficient) : Time complexity = O(n) becacuse for sum function, we have to iterate the nums list n times, space complexity = O(1)

class Solution2:
    def missingNumber(self, nums):
        #To find the sum of natural numbers in the range[1, N]
        # below is the formula:
        # N *(N+1)/2
        n = len(nums)
        total = n(n+1)//2
        sum_of_nums = sum(nums)
        return total - sum_of_nums

answer2 = Solution2()
answer2.missingNumber([0, 1])