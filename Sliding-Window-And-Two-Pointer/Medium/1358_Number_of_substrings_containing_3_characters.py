class Solution:
    # TC = O(n ^ 2)
    def numberOfSubstringBrute1(self, s):
        count = 0
        for i in range(len(s)):
            char_map = [0] * 3
            for j in range(i, len(s)):
                char_map[ord(s[j]) - ord("a")] += 1
                if char_map[0] > 0 and char_map[1] > 0 and char_map[2] > 0:
                    count += 1
        return count

    # TC = O(n ^ 2)
    def numberOfSubstringBrute2(self, s):
        count = 0
        for i in range(len(s)):
            a_count = 0
            b_count = 0
            c_count = 0
            for j in range(i, len(s)):
                if s[j] == "a":
                    a_count += 1
                elif s[j] == "b":
                    b_count -= 1
                else:
                    c_count += 1

                if a_count > 0 and b_count > 0 and c_count > 0:
                    count += 1
        return count

    # TC = O(n)
    # SC = O(3) ==> O(1)
    # the idea is once you find a substring that has all the three characters
    # and after that even if you add as many number of characters to your substring it will only lead
    # to valid substrings
    # So, once you find the element where you condition satisfies you can find the remaining
    # substring by subtracting current valid index from the length of the string, that wil  give
    # you your other substrings
    def numberOfSubstringOptimal(self, s):
        n = len(s)
        l = 0
        r = 0
        char_map = [0] * 3
        result = 0
        while r < n:
            index = ord(s[r]) - ord("a")
            char_map[index] += 1
            while char_map[0] > 0 and char_map[1] > 0 and char_map[2] > 0:
                # length of the string - the current index will
                # give you all the substring which can be found after the
                # r index.
                result += n - r
                char_map[ord(s[l]) - ord("a")] -= 1
                l += 1
            r += 1
        return result


answer = Solution()
s = "abcabc"
s1 = "aaacb"
print(answer.numberOfSubstringBrute1(s1))
print(answer.numberOfSubstringBrute1(s))
print(answer.numberOfSubstringOptimal(s))
