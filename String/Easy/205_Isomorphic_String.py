# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# METHOD 1

# The time complexity of this solution is O(n), where n is the length of the input strings s and t.
# This is because we iterate through the strings once to check if each character is already mapped or not.

# The space complexity is O(k), where k is the number of unique characters in the input strings s and t.
# This is because we use two dictionaries, s_map and t_map, to store the mappings between characters.
# In the worst case, where all characters are unique, the space complexity would be O(n).

class Solution:
    def isIsomorphic(self, s, t):
        s_map = {}
        t_map = {}
        for i, j in zip(s,t):
            if i in s_map and s_map[i] != j:
                return print("False")
            elif j in t_map and t_map[j] != i:
                return print("False")
            s_map[i] = j
            t_map[j] = i
        return print("True")
    
answer = Solution()
answer.isIsomorphic("egg", "bar")

# METHOD 2:

# The time complexity of this solution is O(n^2) because for each character in the string s,
# we are using the index() function which has a time complexity of O(n).
# Since we are doing this for each character in s, the overall time complexity is O(n^2).

# The space complexity is O(n) because we are creating two lists, map1 and map2,
# which can potentially have a length of n (where n is the length of the input strings s and t).
    
class Solution2:
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for i in s:
            map1.append(s.index(i))
        for j in t:
            map2.append(t.index(j))
        if map1 == map2:
            return print("True")
        else:
            return print("False")
        
answer2 = Solution()
answer2.isIsomorphic("egg", "bar")
        
    
    

