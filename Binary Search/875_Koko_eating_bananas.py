import math


# TC = O(log(max) * n) SC = O(1)
class Solution:
    def calculateHours(self, piles, mid, h):
        total_hours = 0
        for p in piles:
            total_hours += math.ceil(p / mid)
        return total_hours

    def minEatingSpeed(self, piles, h):
        l = 1
        r = max(piles)
        res = float("inf")
        while l <= r:
            mid = l + (r - l) // 2
            hours = self.calculateHours(piles, mid, h)
            if hours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


answer = Solution()
piles = [30, 11, 23, 4, 20]
h = 6
print(answer.minEatingSpeed(piles, h))
