class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # def solve(i,j):
        #     if i==0 and j==0: return 1
        #     if i<0 or j<0: return 0
        #     return solve(i-1,j) + solve(i,j-1)
        # return solve(m-1,n-1)

        dp = [[0 for i in range(m)] for j in range(n)]

        for i in range(n):
            dp[i][0] = 1

        for j in range(m):
            dp[0][j] = 1

        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]
            