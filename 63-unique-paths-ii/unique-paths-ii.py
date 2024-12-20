class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1: return 0
        n,m = len(grid), len(grid[0])
        @lru_cache(None)
        def solve(i,j):
            if i==0 and j==0: return 1
            if i<0 or j<0: return 0
            if grid[i][j]==1: return 0
            return solve(i-1,j) + solve(i,j-1)
        
        return solve(n-1,m-1)
