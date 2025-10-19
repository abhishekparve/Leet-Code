# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
# also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
 
# Constraints:
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

# The time complexity of this solution is O(n + m), where n is the length of num1 and m is the length of num2.
# This is because we iterate through both num1 and num2 to convert them into integers. 

# The space complexity is O(1) because we are not using any extra space that grows with the input size.

class Solution:
    def multiplyStrings(self, num1, num2):
        n1 = 0
        n2 = 0
        for i in num1:
            n1 = n1*10 + (ord(i) - 48)
        for j in num2:
            n2 = n2*10 + (ord(j) - 48)
        return str(n1 * n2)

answer = Solution()
result = answer.multiplyStrings("123","456")
print(result)
