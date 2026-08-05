class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        max_length = 1
        i = 0
        j = i + 1

        seen = {}
        seen[s[i]] = 0
        current_length = 1
        while j < len(s):
            if s[j] not in seen:
                seen[s[j]] = j
                current_length += 1
                j += 1
            elif s[j] in seen:
                i = max(i, seen[s[j]] + 1)
                current_length = j - i + 1
                seen[s[j]] = j
                j += 1

            max_length = max(max_length, current_length)

        return max_length      