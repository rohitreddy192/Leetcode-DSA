class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        rows = [-1]*n

        def isPossible(row, j):
            for prev_row in range(row):
                prev_col = rows[prev_row]

                if prev_col == j:
                    return False

                distance = row - prev_row

                if prev_col == j - distance or prev_col == j + distance:
                    return False

            return True

        ans = []
        def solve(board, row):
            if row==n:
                ans.append(["".join(r) for r in board])
                return 
            for j in range(n):
                if isPossible(row, j):
                    board[row][j] = "Q"
                    rows[row] = j 
                    solve(board, row+1)
                    board[row][j] = "."
                    rows[row] = -1

        board = [["." for _ in range(n)] for _ in range(n)]  
        solve(board,0)

        return ans