class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        dp = {}
        def solve(i,j,sum):
            if i<0 or j<0:
                return 0
            if (i,j,sum) in dp: return dp[(i,j,sum)]
            if i==0 and j==0:
                sum += grid[i][j]
                return 1 if sum%k==0 else 0
            
            dp[(i,j,sum)] = (solve(i-1,j,(sum+grid[i][j])%k)%MOD + solve(i,j-1,(sum+grid[i][j])%k)%MOD)%MOD
            return dp[(i,j,sum)]
        
        return solve(len(grid)-1, len(grid[0])-1, 0)%MOD