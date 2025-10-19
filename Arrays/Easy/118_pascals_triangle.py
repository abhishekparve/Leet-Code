# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]

# Time and space complexity of both the methods is O(n^2)

class Solution1:
    def generate(self, numRows):
        result = [[1]]
        for i in range(numRows - 1):
            print(f" length of result[-1]:{len(result[-1])}")
            print(f"result[-1]:{result[-1]}")
            temp = [0] + result[-1] + [0]
            print("temp:", temp)
            rows = []
            for j in range(len(result[-1]) + 1):
                rows.append(temp[j] + temp[j+1])
                print("rows:", rows)
            result.append(rows)
            print("result:", result)
        return print(result)

answer1 = Solution1()
answer1.generate(5)

# Using Math Combinatorics

class Solution2:
    def generate(self, numRows):
        import math
        triangle = []
        for n in range(numRows):
            row = []
            for k in range(n+1):
                row.append(math.comb(n, k))
            triangle.append(row)
        return triangle

answer2 = Solution2()
answer2.generate(5)