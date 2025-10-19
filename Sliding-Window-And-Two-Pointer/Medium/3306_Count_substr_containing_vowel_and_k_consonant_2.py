class Solution:
    # TC = O(n ^ 2)
    # SC = O(1)
    def countOfSubstringsBrute(self, word, k):
        result = 0
        vowel = "aeiou"
        for i in range(len(word)):
            cons_count = 0
            vowel_map = {}
            for j in range(i, len(word)):
                if word[j] in vowel:
                    vowel_map[word[j]] = vowel_map.get(word[j], 0) + 1
                else:
                    cons_count += 1

                if len(vowel_map) == 5 and cons_count == k:
                    result += 1
        return result

    # TC = O(4n)
    # SC = O(n)
    def countOfSubstringsOptimal(self, word, k):
        n = len(word)
        vowel = "aeiou"
        NCI = [n] * n
        cons_index = n
        # O(n)
        for i in range(n - 1, -1, -1):
            if not word[i] in vowel:
                if cons_index != n:
                    NCI[i] = cons_index
                cons_index = i

            else:
                NCI[i] = cons_index

        l = 0
        r = 0
        cons_count = 0
        vowel_map = {}
        result = 0
        # O(n)
        while r < n:
            if word[r] in vowel:
                vowel_map[word[r]] = vowel_map.get(word[r], 0) + 1
            else:
                cons_count += 1
            # O(n)
            while cons_count > k:
                if word[l] in vowel:
                    vowel_map[word[l]] -= 1
                    if vowel_map[word[l]] == 0:
                        del vowel_map[word[l]]
                else:
                    cons_count -= 1
                l += 1
            # O(n)
            while l < n and len(vowel_map) == 5 and cons_count == k:
                result += NCI[r] - r
                if word[l] in vowel:
                    vowel_map[word[l]] -= 1
                    if vowel_map[word[l]] == 0:
                        del vowel_map[word[l]]
                else:
                    cons_count -= 1
                l += 1

            r += 1
        return result


answer = Solution()
word = "ieaouqqieaouqq"
k = 1
print(answer.countOfSubstringsBrute(word, k))
print(answer.countOfSubstringsOptimal(word, k))
