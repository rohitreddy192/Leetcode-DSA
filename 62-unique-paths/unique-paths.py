class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def solve(i,j):
            if i==0 and j==0: return 1
            if i<0 or j<0: return 0
            return solve(i-1,j) + solve(i,j-1)
        return solve(m-1,n-1)