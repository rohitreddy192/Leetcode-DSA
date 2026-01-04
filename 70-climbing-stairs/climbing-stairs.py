class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def solve(i):
            if i<=2: return i
            return solve(i-1) + solve(i-2)
        
        return solve(n)