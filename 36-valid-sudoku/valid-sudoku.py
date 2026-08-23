class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(board,row,col,k):
            for c in range(9):
                if board[c][col] == k:
                    if c!=row:
                        return False
                if board[row][c] == k:
                    if c != col: 
                        return False
                if board[3*(row//3) + c//3][3*(col//3) + c%3] == k:
                    if (row != 3*(row//3) + c//3) and (col != 3*(col//3) + c%3): return False
            return True
        def solve(board):
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] !='.':
                        if isValid(board,row,col,board[row][col]):
                            continue
                        else:
                            return False
            return True
        return solve(board)