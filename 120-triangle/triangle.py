class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)

        def solve(row, col, dp):
            if row==n: return 0
            if (row,col) in dp: return dp[(row,col)]

            dp[(row,col)] =  triangle[row][col] + min(solve(row+1,col,dp), solve(row+1,col+1,dp))
            return dp[(row,col)]

        n = len(triangle)
        dp = {}

        # Base case: beyond the last row
        for col in range(n + 1):
            dp[(n, col)] = 0

        # Bottom-up traversal
        for row in range(n - 1, -1, -1):
            for col in range(row + 1):
                dp[(row, col)] = triangle[row][col] + min(
                    dp[(row + 1, col)],
                    dp[(row + 1, col + 1)]
                )

        return dp[(0, 0)]
