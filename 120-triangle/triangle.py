class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        def solve(i,j):
            if i>len(triangle) or j<0 or j>len(triangle[i]): return float("inf")
            if i==len(triangle)-1: return triangle[i][j]
            if (i,j) in dp: return dp[(i,j)]
            dp[(i,j)] = min(triangle[i][j]+solve(i+1,j), triangle[i][j]+solve(i+1,j+1))
            return dp[(i,j)]
        
        return solve(0,0)