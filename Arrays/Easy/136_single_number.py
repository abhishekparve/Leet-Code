# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1
 
#Method1: hash-map TC = O(n), SC = O(n)

class Solution:
    def singleNumber(self, nums):
        hash_map = {}
        for n in nums:
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1
        for key, value in hash_map.items():
            if value == 1:
                return print(key)
            
answer = Solution()
answer.singleNumber([4,1,2,1,2])

#Method2: hash-map TC = O(n), SC = O(1)
class Solution2:
    def singleNumber(self, nums):
        xor = 0
        for n in nums:
            xor ^= n
        return xor