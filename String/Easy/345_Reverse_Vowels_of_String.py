# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "hello"
# Output: "holle"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# The time complexity of this solution is O(n), where n is the length of the input string.
# This is because we iterate through the string once to convert it into a list,
# and then we iterate through the list once to reverse the vowels.

# The space complexity is O(n) as well. This is because we create a list of length n 
# to store the characters of the input string.

class Solution:
    def reverseVowels(self, s):
        vowels = "AEIOUaeiou"
        m = []
        for x in s:
            m.append(x)
        i = 0
        j = len(m) - 1
        while i < j:
            if m[i] not in vowels:
                i += 1
            elif m[j] not in vowels:
                j -= 1
            elif m[i] in vowels and m[j] in vowels:
                m[i], m[j] = m[j], m[i]
                i += 1
                j -= 1
            
        return print("".join(m))
answer = Solution()
answer.reverseVowels("hello")