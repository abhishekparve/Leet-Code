# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges,
# and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

# Example 1:
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

# The time complexity of this solution is O(n), where n is the length of the input list nums.
# This is because we iterate through the list once in a single for loop.

# The space complexity is O(1) because we only use a constant amount of extra space to store 
# the start, end, and results variables.

class Solution:
    def summaryRanges(self, nums):
        start = nums[0]
        end = nums[0]
        results = []
        for i in range(1, len(nums)):
            print("start: ", start)
            print("end: ", end)
            if (nums[i] > end + 1):
                if start != end:
                    results.append(str(start)+"->"+str(end))
                    print(results)
                else:
                    results.append(str(end))
                    print(results)
                start = nums[i]
                end = nums[i]
            else:
                end = nums[i]
        print("start outer if:", start)
        print("end outer if:", end)
        if start != end:
            results.append(str(start)+"->"+str(end))
            print(results)
        else:
            results.append(str(end))
        return print(results)
            
answer = Solution()
answer.summaryRanges([0,1,2,4,5,7])