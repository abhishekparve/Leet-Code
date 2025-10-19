# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1   Z -> 26
# B -> 2   AA -> 27
# C -> 3   AB -> 28 
# ...      ...

# Example 1:
# Input: columnNumber = 28
# Output: "AB"

# Example 2:
# Input: columnNumber = 701
# Output: "ZY"

# The time complexity of this solution is O(log(columnNumber)) because in each iteration of the while loop,
# we divide the columnNumber by 26 and perform some constant time operations.
# The number of iterations required is equal to the number of digits in columnNumber in base 26,
# which is logarithmic in columnNumber.

# The space complexity of this solution is O(log(columnNumber)) because 
# the result string will have a length equal to the number of digits in columnNumber in base 26,
# which is logarithmic in columnNumber.

class Solution:
    def convertToColumnTitle(self, columnNumber):
        result = ""
        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26
            result += chr(ord("A") + remainder)
            columnNumber = (columnNumber - 1) // 26
        return print(result[::-1])

answer = Solution()
answer.convertToColumnTitle(701)