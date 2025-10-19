class Solution:
    # TC  = O(n ^ 2)
    # SC = O(26)
    def longestSubStringBrute(self, s, k):
        max_length = -1
        for i in range(len(s)):
            charSet = set()
            for j in range(0, len(s)):
                charSet.add(s[j])
                if len(charSet) == k:
                    max_length = max(max_length, j - i + 1)
        return max_length

    # TC  = O(2n)
    # SC = O(26)
    def longestSubStringBetter(self, s, k):
        max_length = -1
        l = 0
        r = 0
        char_map = {}
        while r < len(s):
            char_map[s[r]] = char_map.get(s[r], 0) + 1

            while len(char_map) > k:
                char_map[s[l]] -= 1
                if char_map[s[l]] == 0:
                    del char_map[s[l]]
                l += 1

            if len(char_map) == k:
                max_length = max(max_length, r - l + 1)
            r += 1
        return max_length

    # TC  = O(n)
    # SC = O(26)
    def longestSubStringOptimal(self, s, k):
        max_length = -1
        l = 0
        r = 0
        char_map = {}
        while r < len(s):
            char_map[s[r]] = char_map.get(s[r], 0) + 1

            if len(char_map) > k:
                char_map[s[l]] -= 1
                if char_map[s[l]] == 0:
                    del char_map[s[l]]
                l += 1

            if len(char_map) == k:
                max_length = max(max_length, r - l + 1)
            r += 1
        return max_length


answer = Solution()
s = "aabaaab"
k = 2
print(answer.longestSubStringBrute(s, k))
print(answer.longestSubStringBetter(s, k))
print(answer.longestSubStringOptimal(s, k))
