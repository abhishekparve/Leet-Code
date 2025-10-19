# https://leetcode.com/problems/next-greater-element-i/description/

class Solution:
    # TC = O(m) + O(n^2) SC = O(2n)
    def nextGreaterBrute(self, nums1, nums2):
        map_1 = {val : idx for idx, val in enumerate(nums1)}
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in map_1:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    val = nums2[i]
                    index = map_1[val]
                    res[index] = nums2[j]
                    break
        return print(res)
    # TC = O(m + n) SC = O(3n)
    def nextGreaterOptimal(self, nums1, nums2):
        res = [-1] * len(nums1)
        map_1 = {val : idx for idx, val in enumerate(nums1)}
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                index = map_1[val]
                res[index] = curr
            if curr in map_1:
                stack.append(curr)
        return print(res)
    
    # When there is only one array provided as an input
    # We traverse the given array from the right to left because we are looking for next 
    # greater element towards the right. If we iterate from left to right we will not know all
    # the greater elements on the right side
    # while iterating right to left we will keep on adding the right elements in the stack in the decreasing order
    # If we encounter any element greater than the top of the stack we will keep on poping elemnts from the stack 
    # until the stack is empty or we do not find any element greater than the encountered element in the stack.
    # If we do not find any element we will add -1 in the result array and add the current elemet in the stack and keep
    # on iterating the array.

    # def nextGreaterElement(self, nums):
    #     stack = []
    #     res = []
    #     for i in range(len(nums) -1, -1, -1):
    #         while len(stack)!= 0 and nums[i] >= stack[-1]:
    #             stack.pop()
    #         if len(stack) == 0:
    #             res.append(-1)
    #         else:
    #             res.append(stack[-1])
    #     return print(res)
    
answer = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
nums = [1, 3, 4, 2]
answer.nextGreaterBrute(nums1, nums2)
answer.nextGreaterOptimal(nums1, nums2)
answer.nextGreaterElement(nums)