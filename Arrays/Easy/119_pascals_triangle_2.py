# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]

# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

#Method 1 : Time complexity = O(n) and space complexity = O(rowIndex)
#Solving using binomial coefficients formula
class Solution1:
    def getRow(rowIndex):
        results = [1]
        prev = 1
        for k in range(1, rowIndex + 1):
            next_val = prev *(rowIndex - k + 1) // k
            results.append(next_val)
            prev = next_val
        return print(results)
    
answer = Solution1()
answer.getRow(3)


#Method 2 : Neetcode

class Solution2:
    def getRow(rowIndex):
        results = [1]
        for i in range(rowIndex):
            next_row = [0] * (len(results) + 1)
            for j in range(len(results)):
                next_row[j] += results[j]
                next_row[j+1] += results[j]
            results = next_row
        return print(results)
answer2 = Solution2()
answer2.getRow(3)
