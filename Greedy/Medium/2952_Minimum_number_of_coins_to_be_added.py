class Solution:
    # TC = O(n log n + log(target))
    # SC = O(1)
    def minimumAddedCoins(self, coins, target):
        additions = 0
        maxReach = 0
        index = 0
        # O(n log n)
        coins.sort()
        while maxReach < target:
            if index < len(coins) and coins[index] <= maxReach + 1:
                maxReach += coins[index]
                index += 1
            else:
                # missing smaller number = maxValue + 1
                # maxReach doubles exponentiallly so, O(log(target))
                maxReach += maxReach + 1
                additions += 1
        return additions


answer = Solution()
coins = [1, 4, 10, 5, 7, 19]
target = 19
print(answer.minimumAddedCoins(coins, target))

# NOTE : The same code is used for patching array (LC - 330). There we already have a sorted array
#        so we don't have to sort the array
# If we can form all values up to x, and we now add a coin of value ≤ x + 1,
# then we can extend our coverage to at least x + coin,
# which means now we can reach more numbers.
# If we don’t have such a coin, then to cover the gap between x and x + 1,
# the only option is to add a new coin of value x + 1.

# why this works?
# Let’s say we can make all sums up to x.
# If we encounter a coin that’s greater than x + 1,
# then we cannot make x + 1, which is a missing value.

# So, to cover x + 1, we must add a coin of value x + 1.

# https://leetcode.com/problems/minimum-number-of-coins-to-be-added/solutions/4356100/c-python-java-greedy-explained/
