# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/


class Solution:
    def shipWithDays(self, weights, days):
        l = max(weights)
        r = sum(weights)
        res = r
        while l <= r:
            cap = l + (r - l) // 2
            no_of_days = self.findMinDays(weights, cap)
            if no_of_days <= days:
                res = cap
                r = cap - 1
            else:
                l = cap + 1
        return res

    def findMinDays(self, weights, cap):
        day = 1
        load = 0
        for i in range(len(weights)):
            if load + weights[i] > cap:
                day += 1
                load = weights[i]
            else:
                load += weights[i]
        return day


answer = Solution()
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(answer.shipWithDays(weights, days))
