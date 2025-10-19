# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# The time complexity of this solution is O(max(len(a), len(b))), where a and b are the input binary strings.
# This is because we iterate through the longer string, performing constant time operations for each character.

# The space complexity is O(max(len(a), len(b))) as well.
# This is because we create a new string, "result", to store the binary sum,
# which can be at most as long as the longer input string.

class Solution:
    def addBinary(self, a, b):
        result = ""
        carry = 0
        a = a[::-1]
        b = b[::-1]
        c = max(len(a), len(b))
        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0
            total = digitA + digitB + carry
            char = str(total % 2)
            result = char + result
            carry = total // 2
        
        if carry == "1":
            result = "1" + result
        return print(result)
        
answer = Solution()
answer.addBinary("10101","11")

# Instead of below two lines we can use zfill to add zeros at the beginning
            # zfill will add zeros till the number mentioned in the parameters
            # digitA = digitA.zfill(max(len(a), len(b)))
            # digitB = digitB.zfill(max(len(a), len(b)))