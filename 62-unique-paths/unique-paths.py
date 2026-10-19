class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(i,j,dp):
            if i<0 or j<0: return 0
            if i==0 and j==0: return 1

            if (i,j) in dp: return dp[(i,j)]

            dp[(i,j)]= solve(i-1,j,dp) + solve(i,j-1,dp)

            return dp[(i,j)]

        return solve(m-1,n-1,{})
        