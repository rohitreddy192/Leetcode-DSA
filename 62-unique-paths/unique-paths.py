class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(m,n,dp):
            if m==1 or n == 1: return 1

            if dp[m][n] != -1: return dp[m][n]
            up = solve(m-1,n,dp) 
            left = solve(m,n-1,dp)

            dp[m][n] = left+up
            return dp[m][n]

        dp = [[-1 for i in range(n+1)] for j in range(m+1)]  
        return solve(m,n,dp)
        