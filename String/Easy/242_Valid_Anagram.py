# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# The time complexity of this solution is O(n), where n is the length of the input strings s and t.
# This is because we iterate through both strings once to create the frequency maps.

# The space complexity is O(n) as well, since in the worst case scenario,
# all characters in both strings are unique and we need to store their frequencies in the maps.

# METHOD 1: 
class Solution:
    def validAnagram(self, s, t):
        s_map = {}
        t_map = {}
        if len(s) != len(t):
            return print("False")
        for i in range(len(s)):
            a = s_map.get(s[i], 0)
            b = t_map.get(t[i], 0)
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        for c in s_map:
            if s_map[c] != t_map.get(c, 0):
                return print("False")
        return print("True")
    
answer = Solution()
answer.validAnagram("anagram", "nagaram")


#METHOD 2
# return Counter(s) == Counter(t)
# TC = O(n)
# SC = O(n)

# METHOD 3
# return Sorted(s) == Sorted(t)
# TC = O(nlog(n))
# SC = O(n)
# The space complexity is O(n), where n is the length of the input strings s and t.
# This is because the Sorted function creates a new list to store the sorted characters of the strings.