# https://www.geeksforgeeks.org/problems/square-root/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=square-root


class Solution:
    def findSqrt(self, n):
        l = 1
        r = n
        res = 0
        while l <= r:
            mid = l + (r - l) // 2
            root = mid * mid
            if root < n:
                res = mid
                l = mid + 1
            elif root > n:
                r = mid - 1
            else:
                return mid
        return res


answer = Solution()
n = 5
print(answer.findSqrt(n))
