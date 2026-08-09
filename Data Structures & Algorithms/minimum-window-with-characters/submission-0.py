class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        current = {}    # current substring character frequencies
        required = len(need) # Number of letters we need in the substring
        formed = 0  # Keep track of the current formed substring

        left = 0
        best_length = float('inf')
        best_start = 0

        for right in range(len(s)):
            current[s[right]] = current.get(s[right], 0) + 1

            if s[right] in need and current[s[right]] == need[s[right]]:
                formed += 1

            # Shrink window if we have the required frequencies from left.
            while formed == required:
                window_size = right - left + 1
            
                if window_size < best_length:
                    best_length = window_size
                    best_start = left

                current[s[left]] = current.get(s[left], 0) - 1

                if s[left] in need and current[s[left]] < need[s[left]]:
                    formed -= 1
                
                left += 1

        if best_length == float('inf'):
            return ""

        return s[best_start:best_start+best_length]
