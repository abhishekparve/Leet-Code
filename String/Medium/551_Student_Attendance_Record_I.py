# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.

# Example 1:

# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:

# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

# Time complexity = O(n) | Space complexity = O(1)

class Solution:
    def checkRecord(self, s):
        absent = 0
        late = 0
        for char in s:
            if char == 'A':
                absent += 1
                late = 0
            elif char == 'L':
                late += 1
            else:
                late = 0
            if absent >= 2 or late >= 3:
                return False
        return True
    
answer = Solution()
results = answer.checkRecord("PPALL")
print(results)
