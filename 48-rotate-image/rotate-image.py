class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose(row,col):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        def rowReverse(rowNum):
            matrix[rowNum] = matrix[rowNum][::-1]
        for i in range(len(matrix)):
            for j in range(i):
                transpose(i,j)
        for i in range(len(matrix)):
            rowReverse(i)
        