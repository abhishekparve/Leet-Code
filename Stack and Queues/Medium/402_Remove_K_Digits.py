# https://leetcode.com/problems/remove-k-digits/description/


class Solution:
    # TC = O(n) + O(n) + O(k) = O(2n + k)
    # SC = O(2n)
    def removeKDigits(self, k, num):
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # In context of this problem
        # The general idea behind the greedy algorithm is to remove
        # the larger elements first so that the smaller elements are left

        # But if the input is sorted and the larger elements are not at the
        # start of the input the you will not delete any element in the first
        # pass as it will never enter the while loop

        # but remember the stack will have larger elements at the top in the
        # first pass. So we can remove the last "K" elements to meet the result

        while k > 0:
            stack.pop()
            k -= 1

        res = "".join(stack).lstrip("0")
        return res if res else "0"


answer = Solution()
num = "1432219"
k = 3
print(answer.removeKDigits(k, num))
