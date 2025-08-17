class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def solve(n):
            if n<=2: return n
            return solve(n-1) + solve(n-2)
        return solve(n)