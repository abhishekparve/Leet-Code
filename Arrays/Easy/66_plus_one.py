# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

class Solution1:
    def plus_one(self, digits):
        strings = ""
        for number in digits:
            strings += str(number)
            print (strings)
        temp = str(int(strings) +1)
        print("temp:"+temp)
        print(len(temp))

        return print([int(temp[i]) for i in range(len(temp))])

answer = Solution1()
answer.plus_one([1,2,3])
 