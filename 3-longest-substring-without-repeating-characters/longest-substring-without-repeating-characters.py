class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {i: -1 for i in range(256)}
        cnt = 0
        left = right = 0
        n = len(s)
        while right<n:
            if hm[ord(s[right])] != - 1:
                left = max(left, hm[ord(s[right])]+1)
            hm[ord(s[right])] = right
            cnt = max(cnt,right-left+1)
            right += 1
        return cnt
        