class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend//divisor ==2**31: return 2**31-1
        if dividend//divisor==-2**31: return -1 * 2**31
        return dividend//divisor if (dividend>=0 and divisor>0) or (dividend<0 and divisor<0) else dividend//divisor - (0 if dividend%divisor==0 else (-1 if dividend>0 or divisor>0 else 1))