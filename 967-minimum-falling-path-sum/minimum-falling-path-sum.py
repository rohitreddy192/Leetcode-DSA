class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        @cache
        def solve(i,j):
            if i==0 and 0<=j<m:
                return matrix[i][j]
            if j<0 or j>=m: return float("inf")

            return matrix[i][j] + min(solve(i-1,j), solve(i-1,j-1), solve(i-1,j+1))
        
        mini = float("inf")
        for i in range(m):
            mini = min(mini, solve(n-1,i))
        return mini