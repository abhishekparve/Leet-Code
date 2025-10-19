# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together.
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
#  Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

# Example 1:
# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.

# Example 2:
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

#METHOD 1
# The time complexity of this solution is O(13) because there are 13 key-value pairs
# in the num_map dictionary. The for loop iterates over these 13 values, so the time complexity is constant.

# The space complexity of this solution is O(1) because the num_map dictionary and
# the result string are the only additional space used, and their sizes do not depend on the input size. 
# Therefore, the space complexity is constant.

class Solution:
    def intToRoman(self, num):
        num_map = {
            1:"I", 
            4: "IV", 5:"V",
            9:"IX", 10:"X",
            40:"XL",50:"L",
            90:"XC", 100:"C",
            500:"D", 400:"CD",
            1000:"M", 900:"CM"
        }
        result = ""
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while n <= num:
                result += num_map[n]
                num -= n
        return print(result)
            
            
# answer = Solution()
# answer.intToRoman(58)

#METHOD 2

# The time complexity of this solution is O(1) because the number of iterations in the 
# for loop is constant and does not depend on the input size.
# The space complexity is also O(1) because the size of the num_List is fixed and does not 
# depend on the input size.

class Solution2:
    def intToRoman(self, num):
        num_List = [["I",1],["IV",4],["V",5],["IX",9],["X",10],
                    ["XL",40],["L",50],["XC",90],["C",100],
                    ["CD", 400],["D",500],["CM",900],["M",1000]]
        result = ""
        for sym, value in reversed(num_List):
            if num//value:
                count = num//value
                result += sym * count
                num = num % value
        return print(result)

answer = Solution2()
answer.intToRoman(58)

