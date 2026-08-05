class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        maxFrequency = 0

        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFrequency = max(maxFrequency, count[s[r]])

            if (r - l + 1) - maxFrequency > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result