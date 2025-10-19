# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1?track=DSASP-Searching&amp%253BbatchId=154&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=floor-in-a-sorted-array


# TC = O(log(n)) and SC = O(1)
class Solution:
    def findFloor(self, nums, target):
        l = 0
        r = len(nums) - 1
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res


answer = Solution()
nums = [1, 2, 8, 10, 11, 12, 19]
target = 13
print(answer.findFloor(nums, target))
