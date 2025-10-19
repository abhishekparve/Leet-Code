class Solution:
    def sqrt(self, x):
        l = 1
        r = x
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid < x:
                ans = mid
                l = mid + 1
            elif mid * mid > x:
                r = mid - 1
            else:
                return mid
        return ans

    def sqrtBrute(self, x):
        res = 0
        for i in range(1, x + 1):
            if i * i <= x:
                res = i
            else:
                break
        return res


answer = Solution()
x = 2
# print(answer.sqrt(x))
print(answer.sqrtBrute(x))
