# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either.
# This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached.
# The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0.
# Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range.
# Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.

# Note:
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

# Example 1:
# Input: s = "   -42"
# Output: -42
# Explanation:
# Step 1: "   -42" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -42" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -42" ("42" is read in)
#                ^
# The parsed integer is -42.
# Since -42 is in the range [-231, 231 - 1], the final result is -42.

# Example 2:
# Input: s = "4193 with words"
# Output: 4193
# Explanation:
# Step 1: "4193 with words" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
#              ^
# The parsed integer is 4193.
# Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

#TC = O(n) and space = O(1)

class Solution:
    def myAtoi(self, s):
        # Stripping all the leading white spaces in a string
        s = s.lstrip()
        #If the string is empty then returning 0
        if not s:
            return print(0)
        i = 0
        sign = 1
        # if you find "+" at index 0 then increment i
        # if you find "-" at index 0 then increment i and assign sign as -1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            i += 1
            sign = -1

        parsed = 0
        # Iterating till the length of the string
        # eg = 123
        # when parsed = 0
        #parsed = 0*10 + 1 -> 1
        # when parsed = 1
        #parsed = 1*10 + 2 -> 12
        # when parsed = 12
        #parsed = 12*10 + 1 -> 123
        #This is a method to parse integers in a string
        while i < len(s):
            curr = s[i]
            if not curr.isdigit():
                break
            else:
                parsed = parsed * 10 + int(curr)
            i += 1

        # Multiplying the sign with parsed    
        parsed *= sign

        if parsed > 2**31 - 1:
            return 2**31 - 1
        elif parsed < -2**31:
            return -2**31
        else:
            return print(parsed)

answer = Solution()
answer.myAtoi("4193 with words")