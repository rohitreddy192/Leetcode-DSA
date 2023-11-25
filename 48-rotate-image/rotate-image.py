class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        def reverse(matrix):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])//2):
                    matrix[i][j], matrix[i][-(j+1)] = matrix[i][-(j+1)], matrix[i][j]
        transpose(matrix)
        reverse(matrix) 