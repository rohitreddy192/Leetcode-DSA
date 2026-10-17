class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 1, x
        ans = x
        while l<=h:
            m = (l+h)//2
            if m*m <= x:
                ans = m
                l = m+1
            else:
                h = m-1
        return ans
