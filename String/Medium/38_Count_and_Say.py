# # The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# # countAndSay(1) = "1"
# # countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
# # which is then converted into a different digit string.

# # To determine how you "say" a digit string, split it into the minimal number of substrings
# # such that each substring contains exactly one unique digit. Then for each substring,
# # say the number of digits, then say the digit. Finally, concatenate every said digit.

# Given a positive integer n, return the nth term of the count-and-say sequence.
 
# Example 1:
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.

# Example 2:
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

# The time complexity of this solution is O(2^n) because for each call to the countAndSay function,
# it makes two recursive calls. The space complexity is also O(2^n) because the recursive calls create
# a new stack frame for each call, leading to exponential growth in space usage.

class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        prev = self.countAndSay(n-1)
        result = ""
        count = 1
        for i in range(len(prev)):
            if i == len(prev) - 1 or prev[i] != prev[i+1]:
                result += str(count) + prev[i]  # Append count and character to result
                count = 1
            else:
                count += 1
        return result 

answer = Solution()
result = answer.countAndSay(4)
print(result)