class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        if obstacleGrid[0][0]==1: return 0
        dp = {}
        def solve(i,j):
            if i==0 and j==0: return 1
            if i<0 or j<0: return 0
            if (i,j) in dp: return dp[(i,j)]
            if obstacleGrid[i][j]==1: return 0
            dp[(i,j)] =  solve(i-1,j) + solve(i,j-1)
            return dp[(i,j)]
        return solve(n-1,m-1)