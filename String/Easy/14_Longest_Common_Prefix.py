# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# The time complexity of this solution is O(n*m), where n is the length of the longest string in
# the input list and m is the number of strings in the list. This is because we iterate through each character
# of the longest string in the list, and for each character, we compare it with the corresponding character in each 
# string in the list.

# The space complexity of this solution is O(1) because we only use a constant amount of extra space to store the result string.

class Solution:
    def longestCommonPrefix(self, strs):
        result = ""
        length = len(strs[0])
        for i in range(length):
            for s in strs:
                a = strs[0][i]
                b = s[i]
                if i == len(s) or s[i] != strs[0][i]:
                    return print(result)
            result += strs[0][i]

        return print(result)
    
# answer = Solution()
# answer.longestCommonPrefix(["Flower","Flow","Flight"])
    

# The time complexity of this solution is O(n*m*log(n)), where n is the number of strings in the input list
# and m is the length of the longest string. This is because the solution first sorts the input list,
# which takes O(n*log(n)) time. Then, it iterates through the characters of the first and last strings, which takes O(m) time.
# Therefore, the overall time complexity is O(n*m*log(n)).

# The space complexity of this solution is O(m), where m is the length of the longest string.
# This is because the solution creates a new string called "result" to store the common prefix,
# which can have a maximum length of m. Therefore, the overall space complexity is O(m).

class Solution2:
    def longestCommonPrefix(self, strs):
        result = ""
        sorted_list = sorted(strs)
        first = sorted_list[0]
        print(first)
        last = sorted_list[-1]
        print(last)
        for i in range(len(sorted_list[0])):
            if first[i] != last[i]:
                return print(result)
            result += first[i]
        return print(result)
    
answer = Solution2()
answer.longestCommonPrefix(["Flower","Flow","Flight"])