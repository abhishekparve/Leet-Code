# https://leetcode.com/problems/next-greater-element-ii/


class Solution:
    def nextGreaterElement2(self, nums):
        res = [-1] * len(nums)
        stack = []
        n = len(nums)
        for i in range(2 * n - 1, -1, -1):
            # if stack top is less or equal to curr element then keep poping the stack
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            # When i is less then n then only add elements in the result array
            if i < n:
                if stack:
                    res[i] = stack[-1]
            stack.append(nums[i % n])
        return res


answer = Solution()
nums = [1, 2, 3, 4, 3]
print(answer.nextGreaterElement2(nums))
# Hypothetically double the array
# [1, 2, 1] 1, 2, 1
