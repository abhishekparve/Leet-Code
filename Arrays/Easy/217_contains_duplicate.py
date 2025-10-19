# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


# The time complexity of this solution is O(n), where n is the length of the input list nums.
# This is because we iterate through each element in nums once, performing constant time operations for each element.

# The space complexity of this solution is O(n), where n is the number of unique elements in nums.
# This is because in the worst case scenario, all elements in nums are unique and we store each element in the hash_map dictionary.
class Solution:
    def containsDuplicate(self, nums):
        hash_map = {}
        for n in nums:
            if n in hash_map and hash_map[n] == 1:
                return print("True")
            hash_map[n] = hash_map.get(n, 0) + 1
        return print("False")
    
answer = Solution()
answer.containsDuplicate([1,2,3,4])