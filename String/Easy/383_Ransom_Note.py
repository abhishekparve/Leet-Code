# Given two strings ransomNote and magazine, return true 
# if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# The time complexity of this solution is O(n + m), where n is the length of the ransomNote string
# and m is the length of the magazine string. This is because we iterate through both strings once
# to create the ransomNote_map and magazine_map dictionaries.

# The space complexity of this solution is O(n + m), where n is the number of unique characters
# in the ransomNote string and m is the number of unique characters in the magazine string.
# This is because we store the frequency of each character in the ransomNote and magazine strings
# in the ransomNote_map and magazine_map dictionaries, respectively.
# The space used by these dictionaries will depend on the number of unique characters in each string

class Solution:
    def canConstruct(self, ransomNote, magazine):
        ransomNote_map = {}
        magazine_map = {}
        for i in ransomNote:
            ransomNote_map[i] = ransomNote_map.get(i, 0) + 1
        for j in magazine:
            magazine_map[j] = magazine_map.get(j, 0) + 1
        for key, value in ransomNote_map.items():
            if key not in magazine_map or value > magazine_map[key]:
                return print("False")
        return print("True")
    
answer = Solution()
answer.canConstruct("aa", "ab")