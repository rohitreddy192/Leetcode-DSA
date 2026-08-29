class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = n<0
        n = abs(n)
        @cache
        def solve(n):
            if n==0: return 1
            if n%2 == 0:
                return solve(n//2)*solve(n//2)
            else:
                return x * solve(n-1)
        return solve(n) if not neg else 1/solve(n)
