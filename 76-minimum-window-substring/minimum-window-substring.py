
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = Counter()
        required = len(need)
        formed = 0
        left = 0
        start, minLen = 0, float("inf")

        for right, ch in enumerate(s):
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if right - left + 1 < minLen:
                    start = left
                    minLen = right - left + 1

                c = s[left]
                if c in need and window[c] == need[c]:
                    formed -= 1

                window[c] -= 1
                left += 1

        return "" if minLen == float("inf") else s[start:start + minLen]
