class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        @cache
        def solve(i,j):
            if i<0 or j<0: return 0
            if i==0 and j==0: return 1 if grid[0][0]!=1 else 0
            if grid[i][j]==1: return 0
            return solve(i,j-1) + solve(i-1,j)
        return solve(len(grid)-1,len(grid[0])-1)

        # if grid[0][0]==1: return 0
        # n,m = len(grid), len(grid[0])
        # # @lru_cache(None)
        # # def solve(i,j):
        # #     if i==0 and j==0: return 1
        # #     if i<0 or j<0: return 0
        # #     if grid[i][j]==1: return 0
        # #     return solve(i-1,j) + solve(i,j-1)
        
        # dp = [[0 for i in range(m)] for j in range(n)]
        # dp[0][0] = 0 if grid[0][0]==1 else 1
        # for i in range(1,n):
        #     if grid[i][0] == 1:
        #         dp[i][0] = 0
        #         continue
        #     dp[i][0] = dp[i-1][0]
        # for j in range(1,m):
        #     if grid[0][j] == 1:
        #         dp[0][j] = 0
        #         continue
        #     dp[0][j] = dp[0][j-1]

        # for i in range(1,n):
        #     for j in range(1,m):
        #         if grid[i][j] == 1:
        #             dp[i][j] = 0 
        #             continue
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[n-1][m-1]
