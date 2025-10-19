# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.

# Example 1:
# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

# Example 2:

# Input: s = "Hello"
# Output: 1


# The time complexity of this solution is O(n), where n is the length of the input string s.
# This is because we iterate through each character of the string once.

# The space complexity is O(1) because we only use a constant amount of extra space to store the variables i, c, and count.

# METHOD 1
class Solution:
    def numberOfSegments(self, s):
        n = len(s)
        i = 0
        c = 0
        while i < n:
            while i < n and s[i] == " ":
                i += 1
            count = False
            while i < n and s[i] != " ":
                i += 1
                count = True
                if count:
                    c += 1
                i += 1
        return c

answer = Solution()
answer.numberOfSegments("Hello, my name is John")

# TC = O(n) SC = O(n)

# METHOD 2
class Solution:
    def numberOfSegments(self, s):
        s = s.split()
        return len(s)