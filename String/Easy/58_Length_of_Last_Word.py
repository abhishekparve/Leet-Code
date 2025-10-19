# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Method 1:

# The time complexity of this function is O(n), where n is the length of the input string.
# This is because we iterate through the string once to find the length of the last word.

# The space complexity is O(1) because we only use a constant amount of space to store the length
# and the index variable.

class Solution:
    def lengthOfLastWord(self, s):
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return print(length)
    
answer = Solution()
answer.lengthOfLastWord("Hello World")

# Method 2:

#Time Complexity : O(n) Space Complexity : O(n)

class Solution2:
    def lenghtOfLastWord(self, s):
        result = s.split()
        return print(len(result[-1]))
    
answer = Solution()
answer.lengthOfLastWord("Luffy is the Pirate king")

