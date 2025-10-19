# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

# Example 1:
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.

# Example 2:
# Input: s = "aba"
# Output: false


# Time Complexity:

# The loop runs for all possible substring lengths, which is at most length/2 iterations.
# For each iteration, there is a comparison and string multiplication, both of which take O(length) time.
# Therefore, the overall time complexity is O(length^2).

# Space Complexity:

# The space complexity is O(1) since no additional data structures are used that grow with the input size.

class Solution:
    def repeatedSubstringPattern(self,s):
        length = len(s)

        # Iterate over possible substring lengths
        for i in range(1, length//2 + 1):
            # Check if current substring length divides the string length evenly
            if length % i == 0:
                # Get the current substring
                substring = s[:-1]         
                # Check if the whole string can be formed by repeating the current substring
                if substring * (length // i) == s:
                    return print("True")
        return print("False")

answer = Solution()
answer.repeatedSubstringPattern("abab")

# Time Complexity:

# Concatenating the string with itself takes O(length) time.
# Creating a substring with slicing also takes O(length) time.
# The in operator for strings has a time complexity of O(length), where length is the length of the substring.
# Overall time complexity is O(length).

# Space Complexity:

# The space complexity is O(length) due to the concatenated string.

class Solution2:
    def repeatedSubstringPattern(self,s):
        # Checks if the original string s is a substring of the modified concatenated string (which excludes the first and last characters)
        return s in (s+s)[1:-1]
    
# The purpose of excluding the first and last characters is to avoid considering the original string itself 
# when checking for the presence of s in the concatenated string.

answer = Solution2()
answer.repeatedSubstringPattern("abab")