class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 1, x
        while l<=h:
            m = (l+h)//2
            if m*m <= x:
                l = m+1
            else:
                h = m-1
        return h
