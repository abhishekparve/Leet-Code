# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter
# in pattern and a non-empty word in s.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# METHOD 1 : Using Hash Map
# The time complexity of this solution is O(n), where n is the length of the pattern 
# or the number of words in the string s. This is because we iterate through each character in the pattern
# and each word in the string once.

# The space complexity is O(m), where m is the number of unique characters
# or words in the pattern or string. This is because we store the mapping between characters and 
# words in two dictionaries, which can have at most m entries.

class Solution:
    def wordToPattern(self, pattern, s):
        charToWord = {}
        wordToChar = {}
        word = s.split()
        if len(pattern) != len(word):
            return print("False")
        for c, w in zip(pattern, word):
            if c in charToWord and charToWord[c] != w:
                return print("False")
            if w in wordToChar and wordToChar[w] != c:
                return print("False")
            charToWord[c] = w
            wordToChar[w] = c
        return print("True")
    
answer = Solution()
answer.wordToPattern("abba", "dog cat cat dog")

# METHOD 2

# The time complexity of this solution is O(n), where n is the length of the pattern 
# or the length of the string s.This is because we iterate through each character in 
# the pattern and each word in the string s once.

# The space complexity of this solution is O(n), where n is the length of the pattern 
# or the length of the string s. This is because we create two lists, map1 and map2, 
# which can each have a maximum length of n.

class Solution:
    def wordToPattern(self, pattern, s):
        map1 = []
        map2 = []
        s = s.split()
        for i in pattern:
            map1.append(pattern.index(i))
        for j in s:
            map2.append(s.index(j))
        if map1 == map2:
            return True
        else:
            return False
    
