# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Method 1: time complexity = O(n)
class Solution1:
    def search_insert_position(self, nums, target):
        for i in range(len(nums)):
            if target in nums:
                return print(nums.index(target))
            elif target not in nums:
                nums.append(target)
                nums.sort()
                return print(nums.index(target))
            
answer = Solution1()
answer.search_insert_position([1,3,5,6], 2)

#Method 2 : Time complexity = O(log(n))

class Solution2:
    def search_insert_position(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else :
                return mid
        return left
    
            
