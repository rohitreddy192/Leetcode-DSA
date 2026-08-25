class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix[0]), len(matrix)
        col, row = [1]*(m), [1]*n

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
        
        for i in range(n):
            for j in range(m):
                if row[i]==0 or col[j]==0:
                    matrix[i][j] = 0
        
        