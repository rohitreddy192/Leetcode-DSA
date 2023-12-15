class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(board,row,col,k):
            for c in range(9):
                if board[c][col] == k:
                    return False
                if board[row][c] == k:
                    return False
                if board[3*(row//3) + c//3][3*(col//3) + c%3] == k:
                    return False
            return True
        def solve(board):
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] =='.':
                        for i in range(1,10):
                            if isValid(board,row,col,str(i)):
                                board[row][col] = str(i)
                                if solve(board) == True:
                                    return True
                                else:
                                    board[row][col] = '.'
                        return False
            return True
        solve(board)