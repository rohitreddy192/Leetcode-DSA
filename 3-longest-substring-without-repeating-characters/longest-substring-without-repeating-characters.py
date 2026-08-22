class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()

        n = len(s)
        l,r = 0,0 
        maxi = 0
        while r<n:
            if s[r] not in hs:
                hs.add(s[r])
                r += 1
            else:
                hs.remove(s[l])
                l += 1
            maxi = max(maxi, r-l)
        
        return maxi