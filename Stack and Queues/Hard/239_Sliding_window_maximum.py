# https://leetcode.com/problems/sliding-window-maximum/description/

from collections import deque


class Solution:
    def maxSlidingWindowBrute(self, nums, k):
        n = len(nums)
        result = []
        # how come n - k + 1 ?
        # n is length of nums
        # k is the size of the window
        # for below example
        # nums = [1,3,-1,-3,5,3,6,7]
        # n = 8 and k = 3
        # so 8 - 3 + 1 = 6
        # which means there will be six windows in total
        # [0: 3] at index 0, [1:4], [2:5], [3:6],[4:7],[5:8]
        # so you are maintaining the window size of 3
        for i in range(0, n - k + 1):
            maxVal = nums[i]
            for j in range(i, k + i):
                maxVal = max(nums[j], maxVal)
            result.append(maxVal)
        return result

    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        res = []
        window = deque()
        for i in range(len(nums)):
            # Step 1
            # whenever a new element comes in check if the window size is present
            # to insert that element or not. dequeue.front <= (i - k). Any element in the
            # front which is less than or equl to i - k should be popped out
            if window and window[0] <= i - k:
                window.popleft()
            # Step 2
            # check if the current elem is greater than dequeue.back element
            # if yes, the pop the smaller dequeue.back element as we are storing
            # the elements in the monotonic decreasing fashion
            while window and nums[i] > nums[window[-1]]:
                window.pop()
            # Step 3
            # append the index of the element in the dequeue
            window.append(i)
            # Step 4
            # We will start getting the answers whenever our i will be greater
            # than window size which is k - 1. So append the dequeue.front element to the
            # result.
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


answer = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(answer.maxSlidingWindowBrute(nums, k))
print(answer.maxSlidingWindow(nums, k))
