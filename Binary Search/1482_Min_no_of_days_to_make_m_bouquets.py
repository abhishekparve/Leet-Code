class Solution:
    def minDays(self, bloomDays, m, k):
        l = 0
        r = max(bloomDays)
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            bouquets = self.calculateBouquets(bloomDays, k, mid)
            if bouquets >= m:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

    def calculateBouquets(self, bloomDays, k, mid):
        adj_count = 0
        bouq_count = 0
        for i in range(len(bloomDays)):
            if mid >= bloomDays[i]:
                adj_count += 1
            else:
                adj_count = 0
            if adj_count == k:
                bouq_count += 1
                adj_count = 0
        return bouq_count


answer = Solution()
bloomDays = [7, 7, 7, 7, 12, 7, 7]
m = 2
k = 3
print(answer.minDays(bloomDays, m, k))
