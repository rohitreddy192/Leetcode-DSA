class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def solve(i,j):
            if i<0 or j<0: return float("inf")
            if i==0 and j==0: return grid[0][0]
            
            return grid[i][j] + min(solve(i-1,j), solve(i,j-1))

        return solve(len(grid)-1,len(grid[0])-1)