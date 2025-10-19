#Majority duplicate elements

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Follow-up: Could you solve the problem in linear time and in O(1) space?

# Time complexity = O(n) spave complexity = O(n)
# Any opertion on hash-map the time-complexity is O(n) but we are using a data structure hash-map the space complexity = O(n)
class Solution1:
    def majority_duplicates(self, nums):
        count = {}
        result, maxCount = 0,0
        for n in nums:
            count[n] = 1 + count.get(n,0)
            # print(count)
            if count[n] > maxCount:
                # print(count[n])
                result = n
                #print(f"n:{n},result:{result},maxCount:{maxCount}")
            else:
                result
                # print (f"result else loop:{result}")
            maxCount = max(count[n], maxCount)
        return print(result)
answer = Solution1()
answer.majority_duplicates([2,3,3,4, 2, 3, 3, 3, 6, 2])

# Without using hash-map
#  Time complexity = O(n) spave complexity = O(1)
class Solution2:
    def majority_duplicates(self, nums):
        result, count = 0,0
        for n in nums:
            if count == 0:
                result = n
            if n == result:
                count += 1
            else:
                count -= 1
        return print(result)

answer2 = Solution2()
answer2.majority_duplicates([2,3,3,4, 2, 3, 3, 3, 6, 2])

       