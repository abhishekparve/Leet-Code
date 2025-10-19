# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

# The time complexity of this solution is O(n), where n is the length of the input string.
# This is because we iterate through the string once to build the frequency map, and then
# iterate through the string again to find the first unique character.

# The space complexity is O(k), where k is the number of unique characters in the input string.
# This is because we store the frequency of each character in the s_map dictionary. In the worst case,
# where all characters in the string are unique, the space complexity would be O(n).
# However, in practice, the number of unique characters is typically much smaller than the length of the string.

class Solution:
    def firstUniqChar(self, s):
        s_map = {}
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
        for i in range(len(s)):
            if s_map[s[i]] == 1:
                return i
        return -1
    
answer = Solution()
answer.firstUniqChar("leetcode")