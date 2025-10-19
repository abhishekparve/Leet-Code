class Solution:
    # TC = O(n ^ 2)
    # SC = O(26)
    def characterReplacementBrute(self, s, k):
        max_length = 0
        for i in range(len(s)):
            charFreq = [0] * 26
            maxFreq = 0
            for j in range(i, len(s)):
                # ord('A') is 65 and B is 66 and so on...
                index = ord(s[j]) - ord("A")
                charFreq[index] += 1
                maxFreq = max(maxFreq, charFreq[index])
                # No of replacements needed
                # window_size - maxFreq of element
                if (j - i + 1) - maxFreq <= k:
                    max_length = max(max_length, j - i + 1)
        return max_length

    # TC = O(n + n) * 26
    # SC = O(26)
    def characterReplacementBetter(self, s, k):
        l = 0
        r = 0
        maxFreq = 0
        max_length = 0
        charFreq = [0] * 26
        while r < len(s):
            # updating the charFreq
            index = ord(s[r]) - ord("A")
            charFreq[index] += 1
            # Calculating the maxFreq
            maxFreq = max(maxFreq, charFreq[index])
            # If the window_size - maxFreq of elem in the Sliding window
            # is greater than k, then keep dcrementing the window by
            # shifting the right pointer
            while (r - l + 1) - maxFreq > k:
                # decrement the char freq of the elem at l pointer in the charFreq array by 1
                charFreq[ord(s[l]) - ord("A")] -= 1
                maxFreq = 0
                # After the decrement again calculate the maxFreq in the entire charFreq array
                for i in range(len(charFreq)):
                    maxFreq = max(maxFreq, charFreq[i])
                l += 1
            # If the condition meets then calculate the length
            # replacements = window_size - maxFreq of elem in the Sliding window
            if (r - l + 1) - maxFreq <= k:
                max_length = max(max_length, r - l + 1)
            r += 1
        return max_length

    # TC = O(n) * 26
    # SC = O(26)
    def characterReplacementOptimal(self, s, k):
        l = 0
        r = 0
        maxFreq = 0
        max_length = 0
        charFreq = [0] * 26
        while r < len(s):
            index = ord(s[r]) - ord("A")
            charFreq[index] += 1
            maxFreq = max(maxFreq, charFreq[index])
            # No need to decrement the maxFreq because it will not contribut to the max_length
            # we want a substring of max length. Decrementing the max_length will lead to
            # unnecessary computation of strings with smaller length.

            # If the window_size - maxFreq of elem in the Sliding window
            # is greater than k, then keep dcrementing the window by
            # shifting the right pointer
            if (r - l + 1) - maxFreq > k:
                # decrement the char freq of the elem at l pointer in the charFreq array by 1
                charFreq[ord(s[l]) - ord("A")] -= 1
                l += 1
            # If the condition meets then calculate the length
            # replacements = window_size - maxFreq of elem in the Sliding window
            if (r - l + 1) - maxFreq <= k:
                max_length = max(max_length, r - l + 1)
            r += 1
        return max_length


answer = Solution()
s = "AABABBA"
k = 1
print(answer.characterReplacementBrute(s, k))
print(answer.characterReplacementBetter(s, k))
print(answer.characterReplacementOptimal(s, k))
