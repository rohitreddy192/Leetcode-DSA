class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        l = 0
        r = 0
        maxi = 0
        for i in s:
            if i =="(":
                l += 1
            else:
                r += 1
            if l==r:
                maxi = max(maxi, r*2)
            if l<r:
                l = 0
                r=0
        l,r = 0, 0
        for i in reversed(s):
            if i ==")":
                r += 1
            else:
                l += 1
            if l==r:
                maxi = max(maxi, r*2)
            if l>r:
                l = 0
                r=0
        return maxi
        
        