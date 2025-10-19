# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or
# equal to k characters, then reverse the first k characters and leave the other as original.

# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"

#METHOD 1:
# TC = O(n) SC = O(n)

class Solution:
    def reverseStr(self, s, k):
        s = list(s)
        for i in range(0, len(s), 2*k):
            start = i
            end = min(i + k - 1, len(s) - 1)
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        result = "".join(s)
        return print(result)

answer = Solution()
answer.reverseStr("abcdefg", 2)

#METHOD 2

# TC = O(n) SC = O(n)
class Solution2:
    def reverseStr(self, s, k):
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i+k] = s[i:i+k][::-1]
        result = "".join(s)
        return print(result)
    
answer = Solution2()
answer.reverseStr("abcdefg", 2)