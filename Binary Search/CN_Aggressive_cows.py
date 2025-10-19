# https://www.naukri.com/code360/problems/aggressive-cows_1082559?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse


class Solution:
    # 0(nlog(n) + (max(stalls) - min(stalls))*n)
    def maxDistanceBrute(self, stalls, k):
        # Sorting the stalls
        stalls.sort()
        # length of stalls/array
        n = len(stalls)
        # max possible distance between two cows
        limit = stalls[n - 1] - stalls[0]
        for i in range(1, limit + 1):
            if not self.canPlaceCows(stalls, i, k):
                return i - 1
        return limit

    # 0(log(n) + log(max(stalls) - min(stalls))*n)
    def maxDistanceOptimal(self, stalls, k):
        stalls.sort()
        n = len(stalls)
        l = 1
        r = stalls[n - 1] - stalls[0]
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if self.canPlaceCows(stalls, mid, k):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res

    def canPlaceCows(self, stalls, dist, cows):
        lastCow = stalls[0]
        cowCount = 1
        for i in range(1, len(stalls)):
            if stalls[i] - lastCow >= dist:
                cowCount += 1
                lastCow = stalls[i]
            if cowCount >= cows:
                return True
        return False


stalls = [0, 3, 4, 7, 10, 9]
k = 4
answer = Solution()
print(answer.maxDistanceBrute(stalls, k))
