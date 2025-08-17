class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]==1: return 0
        @cache
        def solve(i,j):
            if i==0 and j==0: return 1
            if i<0 or j<0 or obstacleGrid[i][j]==1: return 0
            return solve(i-1,j) + solve(i,j-1)
        return solve(n-1,m-1)