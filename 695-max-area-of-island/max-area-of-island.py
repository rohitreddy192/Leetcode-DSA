class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0

            if grid[r][c] == 0:
                return 0

            # Mark as visited
            grid[r][c] = 0

            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        ans = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))

        return ans