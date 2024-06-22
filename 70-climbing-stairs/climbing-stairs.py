class Solution:
    def climbStairs(self, n: int) -> int:
        a0, a1 = 1, 1
        for i in range(1,n+1):
            temp = a0
            a0 = a1
            a1 = a1 + temp
        return a0