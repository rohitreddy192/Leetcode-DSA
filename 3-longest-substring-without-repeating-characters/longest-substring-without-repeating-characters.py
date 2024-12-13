class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        n = len(s)
        seen = set()
        maxi = 0
        while right < n and left<=right:
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
            maxi = max(right-left, maxi)
        return maxi