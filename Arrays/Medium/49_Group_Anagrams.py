# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

''' The time complexity of this solution is O(n * m),
where n is the number of strings in the input list and m is the average length of the strings.
This is because for each string, we iterate through its characters to count the frequency of each character,
which takes O(m) time. Since we do this for each string in the input list, the overall time complexity is O(n * m).

The space complexity of this solution is O(n * m),
where n is the number of strings in the input list and m is the average length of the strings.
This is because we use a defaultdict to store the grouped anagrams,
where the keys are tuples representing the frequency counts of characters in each string. 
The size of the defaultdict is proportional to the number of unique frequency count tuples,
which can be up to O(n * m) in the worst case.
Additionally, each string is stored in the defaultdict as a value, so the overall space complexity is O(n * m).'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        print(result.values())

# Without using defaultdict
class Solution2:
    def groupAnagrams(self, strs):
        result = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key in result:
                result[key].append(s)
            else:
                result[key] = [s]
        print(result.values())

answer = Solution()
answer2 = Solution2()
# answer.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
answer2.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
