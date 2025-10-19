# A valid IP address consists of exactly four integers separated by single dots.
# Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
# but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed
# by inserting dots into s. You are not allowed to reorder or remove any digits in s.
# You may return the valid IP addresses in any order.

 
# Example 1:

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:

# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:

# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

"""

Time Complexity:

The function backtrack is called recursively to generate all possible valid IP addresses.
In the worst-case scenario, each digit of the input string s is considered for each segment of the IP address.
There are at most 3 choices for each segment (except for the first one where there's no leading zero allowed). Hence, for each segment, there can be at most 3 iterations in the inner loop.
Since there are 4 segments in an IP address, the time complexity for generating all possible IP addresses is bounded by O(3^4) = O(81).
However, not every sequence of digits generates a valid IP address. The check int(s[i:j+1]) < 256 ensures that the segments don't exceed 255. Additionally, the condition (i == j or s[i] != "0") ensures that no leading zeros are considered except for the first segment.
Despite these conditions, the overall time complexity remains bounded by O(3^4).
Thus, the time complexity of the restoreIpAddresses function is O(1) since it doesn't depend on the size of the input.

Space Complexity:

The space complexity mainly depends on the recursion depth, which in turn depends on the number of valid IP addresses generated.
At each level of recursion, backtrack function appends a potential IP address to the result list. The length of this list represents the space needed to store all valid IP addresses.
In the worst-case scenario, where all combinations of digits form valid IP addresses, the number of valid IP addresses can be bounded by O(3^4), hence, the space complexity would be O(3^4).
Additionally, there's auxiliary space used for storing intermediate variables, but they don't dominate the overall space complexity.
Thus, the space complexity of the restoreIpAddresses function is O(1), disregarding the space used for the result list.
"""

class Solution:
    def restoreIPAddresses(self, s):
        result = []
        if len(s) > 12:
            return result
        def backTrack(i, dots, currIp):
            if dots == 4 and i == len(s):
                result.append(currIp[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i + 3, len(s))):
                if (int(s[i: j+1]) < 256 and (i == j or s[i] != "0")):
                    backTrack(j + 1, dots + 1, currIp + s[i : j + 1] + ".")
        backTrack(0, 0, "")
        return result

answer = Solution()
result = answer.restoreIPAddresses("25525511135")
print(result)
