class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(i,j,dp):
            if i==0 and j==0: return 1
            if i<0 or j<0: return 0
            if dp[i][j] !=-1: return dp[i][j]

            up = solve(i,j-1,dp)
            left = solve(i-1,j,dp)
            
            dp[i][j] = up+left
            return up + left
        dp = [[-1 for i in range(n)]for j in range(m)]
        return solve(m-1,n-1,dp)