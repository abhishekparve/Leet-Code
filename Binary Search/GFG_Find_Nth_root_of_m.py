class Solution:
    def calculateRoot(self, n, mid):
        root = 0
        root = mid**n
        return root

    def findNthRoot(self, n, m):
        l = 1
        r = m
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            root = self.calculateRoot(n, mid)
            if root == m:
                return mid
            elif root > m:
                r = mid - 1
            else:
                l = mid + 1
        return res


answer = Solution()
n = 3
m = 9
print(answer.findNthRoot(n, m))
