class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)

        @cache
        def solve(row, col):
            if row==n: return 0

            return triangle[row][col] + min(solve(row+1,col), solve(row+1,col+1))

        return solve(0,0)