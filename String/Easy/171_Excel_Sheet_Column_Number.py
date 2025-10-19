# Given a string columnTitle that represents the column title as appears in an Excel sheet,
# return its corresponding column number.

# For example:

# A -> 1   Z -> 26
# B -> 2   AA -> 27
# C -> 3   AB -> 28 
# ...      ...

# Example 1:
# Input: columnTitle = "AB"
# Output: 28

# Example 2:
# Input: columnTitle = "ZY"
# Output: 701

# The time complexity of this solution is O(n), where n is the length of the columnTitle string.
# This is because we iterate through the string once to calculate the corresponding value for each character.

# The space complexity is O(1) because we only use a constant amount of extra space to store the result
# and the variables used in the calculation.

class Solution:
    def titleToNumber(self, columnTitle):
        result = 0
        p = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            # B + 1 * 26^0
            # How to get B
            # ord("B") - ord("A")
            x = ord(columnTitle[i]) - ord("A") + 1
            x = x*26**p
            result += x
            p += 1
        return print(result)
    
#ascii value of A is 65 and B is 66
# therefore, 65- 66 = 1 but we need the value for B so we add 1
    
answer = Solution()
answer.titleToNumber("AB")

