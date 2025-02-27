class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        @lru_cache(None)
        def solve(i,j):
            if i<0 or j<0: return 0
            if matrix[i][j] == "1":
                return 1 + min(solve(i-1,j), solve(i,j-1), solve(i-1,j-1))
            return 0
        mx = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mx = max(mx, solve(i,j))
        
        return mx*mx