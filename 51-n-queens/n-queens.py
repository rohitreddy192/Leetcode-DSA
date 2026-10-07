class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        matrix = [["." for _ in range(n)] for _ in range(n)]
        ans = []

        def isSafe(i, j):

            # Column
            for idx in range(n):
                if matrix[idx][j] == "Q":
                    return False

            # Upper-left and upper-right diagonals
            for di, dj in [(-1, -1), (-1, 1)]:
                ddi, ddj = i + di, j + dj

                while 0 <= ddi < n and 0 <= ddj < n:
                    if matrix[ddi][ddj] == "Q":
                        return False

                    ddi += di
                    ddj += dj

            return True

        def solve(i):
            if i == n:
                ans.append(["".join(row) for row in matrix])
                return

            for j in range(n):

                if isSafe(i, j):

                    matrix[i][j] = "Q"

                    solve(i + 1)

                    # BACKTRACK
                    matrix[i][j] = "."

        solve(0)

        return ans