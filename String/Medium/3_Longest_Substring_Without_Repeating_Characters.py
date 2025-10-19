# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.


# TC = O(n) and SC = O(n)
class Solution:
    # TC = O(n^3) and SC = O(n)
    def lengthOfLongestSubstringBrute(self, s):
        length = 0
        for i in range(len(s)):
            res = ""
            for j in range(len(s)):
                if s[j] in res:
                    break
                res += s[j]
                length = max(length, len(res))
        return length

    # Using Set
    # TC = O(n)
    def lengthOfSubstring(self, s):
        length = 0
        l = 0
        charSet = set()
        for r in range(len(s)):
            char = s[r]
            while char in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(char)
            length = max(length, r - l + 1)
        return length

    def lengthOfLongestSubstring(self, s):
        seen = {}
        length = 0
        l = 0
        if not s:
            return 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                # r - l + 1 is used to calculate the length of the sliding window
                length = max(length, r - l + 1)
            seen[char] = r
        return print(length)


answer = Solution()
# answer.lengthOfLongestSubstring("abcabcbb")
# print(answer.lengthOfLongestSubstringBrute("abcabcbb"))
print(answer.lengthOfSubstring("abcabcbb"))
