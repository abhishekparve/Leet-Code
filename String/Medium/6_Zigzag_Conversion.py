# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"

#METHOD 1:
# The time complexity of this solution is O(n), where n is the length of the input string s. 
# This is because we iterate through each character in the string once.

# The space complexity is O(n), as we create a list of length numRows to store the characters in each row.
# Additionally, we create a string of length n to store the final result.

class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows > len(s):
            return print(s)
        result = ""
        rows = [[] for row in range(numRows)]
        step = 1
        index = 0
        for char in s:
            result[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        for i in range(numRows):
            rows[i] = "".join(rows[i])
        result = "".join(rows)
        return print(result)

# answer = Solution()
# answer.convert("PAYPALISHIRING")

#METHOD 2
# The time complexity of this solution is O(n), where n is the length of the input string s.
# This is because we iterate through each character in the string once.

# The space complexity is O(n) as well. This is because we create a new string called "result" to store
# the converted string, and the length of this string will be the same as the length of the input string s.

class Solution2:
    def convert(self, s, numRows):
        result = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                result += s[i]
                if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                    result += s[i + increment - 2 * r]
        return print(result)
    
answer = Solution2()
answer.convert("PAYPALISHIRING", 4)


