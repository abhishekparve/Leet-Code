# You are given a positive integer n. A binary string x is valid if all substringsof x of length 2 contain at least one "1".

# Return all valid strings with length n, in any order.

# Example 1:

# Input: n = 3
# Output: ["010","011","101","110","111"]

# Explanation:
# The valid strings of length 3 are: "010", "011", "101", "110", and "111".

# Example 2:

# Input: n = 1
# Output: ["0","1"]

# Explanation:
# The valid strings of length 1 are: "0" and "1".

# Constraints:
# 1 <= n <= 18


def generateAllBinaryStrings(n):

    def generateStrings(currStr, index):
        if index == n:
            return [currStr]

        result = []

        if not currStr or currStr[-1] == "1":
            result += generateStrings(currStr + "0", index + 1)
        result += generateStrings(currStr + "1", index + 1)

        return result

    return generateStrings("", 0)


n = 3

# print(generateAllBinaryStrings(k))
result = generateAllBinaryStrings(n)
print(result)

# Practise code:

# def generate(currStr, index, res):
#     if index == k:
#         res += currStr
#         return

#     generate(currStr + "0", index + 1, res)

#     if not currStr or currStr[-1] != "1":
#         generate(currStr + "1", index + 1, res)
