class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        @cache
        def solve(i,j):
            if i==n-1 and 0<=j<n: return triangle[i][j]
            if j<0 or j>=n: return float("inf")

            return triangle[i][j] + min(solve(i+1,j), solve(i+1,j+1))

        return solve(0,0)