class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        def solve(i,j):
            if j>=len(triangle[i]):
                return float("inf")
            if i==n-1:
                return triangle[i][j]
            
            return triangle[i][j] + min(solve(i+1,j),solve(i+1,j+1))
        
        return solve(0,0)