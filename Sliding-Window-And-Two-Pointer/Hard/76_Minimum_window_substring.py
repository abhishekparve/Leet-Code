class Solution:
    # TC = O(n ^ 2)
    def minWindowBrute(self, s, t):
        res = ""
        min_length = float("inf")
        for i in range(len(s)):
            t_map = {}
            count = 0
            for k in range(len(t)):
                t_map[t[k]] = t_map.get(t[k], 0) + 1
            for j in range(i, len(s)):
                if s[j] in t_map and t_map[s[j]] > 0:
                    t_map[s[j]] -= 1
                    count += 1
                if count == len(t):
                    length = j - i + 1
                    if length < min_length:
                        res = s[i : j + 1]
                        min_length = length
                    else:
                        break
        return res

    # TC = O(m + n)
    # SC = O(m + n)
    # Neetcode Solution
    def minWindowNeetcode(self, s, t):
        if len(t) > len(s):
            return ""

        t_map = {}
        for i in range(len(t)):
            t_map[t[i]] = t_map.get(t[i], 0) + 1

        window = {}
        l = 0
        r = 0
        res = [-1, -1]
        min_length = float("inf")
        have = 0
        # need contains the count of unique element in t_map
        need = len(t_map)

        while r < len(s):
            char = s[r]
            if char in t_map:
                window[char] = window.get(char, 0) + 1
                if window[char] == t_map[char]:
                    have += 1

            while have == need:
                # Calculate the min_length
                if (r - l + 1) < min_length:
                    res = [l, r]
                    min_length = r - l + 1

                # Shrink the window from the left
                if s[l] in t_map:
                    window[s[l]] -= 1
                    # If you have removed the required char from the
                    # window, then its count will be less than the existing
                    # count in t_map
                    if window[s[l]] < t_map[s[l]]:
                        have -= 1
                l += 1
            r += 1
        # It takes the list res and assigns:
        # l = res[0] (start index of the best window found)
        # r = res[1] (end index of the best window found)
        l, r = res

        return s[l : r + 1] if min_length != float("inf") else ""

    # TC = O(m + n)
    # SC = O(m)
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""
        t_map = {}
        for i in range(len(t)):
            t_map[t[i]] = t_map.get(t[i], 0) + 1
        l = 0
        r = 0
        required_count = 0
        min_length = float("inf")
        while r < len(s):
            char = s[r]
            if char in t_map:
                t_map[char] -= 1
                if t_map[char] == 0:
                    required_count += 1

            while required_count == len(t_map):
                # Calculate length of the window
                if (r - l + 1) < min_length:
                    result = s[l : r + 1]
                    min_length = r - l + 1

                # Shrink the window from left
                if s[l] in t_map:
                    t_map[s[l]] += 1
                    if t_map[s[l]] > 0:
                        required_count -= 1
                l += 1
            r += 1

        return result if min_length != float("inf") else ""


answer = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(answer.minWindowBrute(s, t))
print(answer.minWindowNeetcode(s, t))
print(answer.minWindow(s, t))
