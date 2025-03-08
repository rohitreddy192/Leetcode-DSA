class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def solve(i,j):
            if i>=len(matrix) or j<0 or j>=len(matrix[0]): return float("inf")
            if i == len(matrix)-1: return matrix[i][j]
            return matrix[i][j] + min(solve(i+1,j),solve(i+1,j+1), solve(i+1,j-1))
        
        mini = float("inf")
        for i in range(len(matrix[0])):
            mini = min(mini, solve(0,i))
        return mini