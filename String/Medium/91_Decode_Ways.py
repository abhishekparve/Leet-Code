class Solution:
    def decodeWays(self, s):
        dp = {len(s):1}
        def dfs(i):
            if i in dp:
                a = dp[i]
                return dp[i]
            if s[i] == "0":
                return 0
            result = dfs(i + 1)
            if (i + 1 < len(s) and int(s[i] + s[i + 1]) in range(10,  27)):
                result += dfs(i+2)
            dp[i] = result
            return result
        return dfs(0)

answer = Solution()
result = answer.decodeWays("1201234")
print(result)
            