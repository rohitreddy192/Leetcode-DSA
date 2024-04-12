class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        left = right = 0
        cnt = 0
        
        while right<len(s):
            while s[right] in hs:
                hs.remove(s[left])
                left += 1
            hs.add(s[right])
            
            cnt = max(cnt,right-left+1)
            right += 1
            
        return cnt
        