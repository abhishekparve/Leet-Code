# https://www.geeksforgeeks.org/problems/ceil-the-floor2802/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=ceil-the-floor


# Approach 2
# TC = O(log(n)) and SC = O(1)
class Solution:
    def ceilTheFloor(self, nums, target):
        l = 0
        r = len(nums) - 1
        floor = -1
        ceil = float("inf")
        result = []
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                floor = max(floor, nums[mid])
                l = mid + 1
            elif nums[mid] > target:
                ceil = min(ceil, nums[mid])
                r = mid - 1
        if ceil == float("inf"):
            ceil = -1
        result.append(floor)
        result.append(ceil)
        return result


answer = Solution()
nums = [5, 6, 8, 9, 6, 5, 5, 6]
target = 7
print(answer.ceilTheFloor(nums, target))
