class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n, m = len(triangle), len(triangle[0])
        @cache
        def solve(i,j):
            if i==n:
                return 0
            
            return triangle[i][j] + min(solve(i+1,j), solve(i+1,j+1))

        return solve(0,0)