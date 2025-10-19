# https://www.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1


class Solution:
    def minimumNumberOfCoins(self, n):
        denomination = [1, 2, 5, 10]
        count = 0
        for i in range(len(denomination) - 1, -1, -1):
            while n >= denomination[i]:
                n -= denomination[i]
                count += 1
        return count


answer = Solution()
n = 39
print(answer.minimumNumberOfCoins(n))

"""
To minimize the number of coins required, we should always pick the largest possible denomination first
and then move to smaller ones. This ensures that the total coins used are minimum.
"""
