class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        rows = []
        cols = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        rows.sort()
        cols.sort()

        row = rows[len(rows) // 2]
        col = cols[len(cols) // 2]

        ans = 0

        for r in rows:
            ans += abs(r - row)

        for c in cols:
            ans += abs(c - col)

        return ans