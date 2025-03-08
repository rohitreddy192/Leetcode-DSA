class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def solve(i,j):
            if i>len(triangle) or j<0 or j>len(triangle[i]): return float("inf")
            if i==len(triangle)-1: return triangle[i][j]
            return min(triangle[i][j]+solve(i+1,j), triangle[i][j]+solve(i+1,j+1))
        
        return solve(0,0)