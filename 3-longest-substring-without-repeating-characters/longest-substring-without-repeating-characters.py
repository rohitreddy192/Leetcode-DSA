class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        n = len(s)
        i = 0
        maxi = 0
        for j in range(n):
            while s[j] in hs:
                hs.remove(s[i])
                i += 1
            
            maxi = max(maxi, j-i+1)
            hs.add(s[j])
        return maxi