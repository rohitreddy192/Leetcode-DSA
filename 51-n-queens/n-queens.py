class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(col,row,board):
            left = col
            while left>=0:
                if board[row][left] == "Q": return False
                left -= 1
            left = col
            up = row
            down = row
            while left>=0:
                if up>=0:
                    if board[up][left] == "Q": return False
                    up -= 1
                if down<n:
                    if board[down][left]=="Q": return False
                    down+=1
                left -= 1
            return True
        def solve(col, board, ans):
            if col == n:
                l = list()
                for i in board:
                    l.append("".join(i))
                ans.append(tuple(l))
                return
            
            for i in range(n):
                if isSafe(col,i,board):
                    print(board)
                    board[i][col] = "Q"
                    solve(col+1, board, ans)
                    board[i][col] = "."
                
        board = [["." for i in range(n)] for j in range(n)]
        ans = []
        solve(0,board,ans)
        return ans

