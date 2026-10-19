class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)

        def solve(row, col, dp):
            if row==n: return 0
            if (row,col) in dp: return dp[(row,col)]

            dp[(row,col)] =  triangle[row][col] + min(solve(row+1,col,dp), solve(row+1,col+1,dp))
            return dp[(row,col)]

        return solve(0,0,{})