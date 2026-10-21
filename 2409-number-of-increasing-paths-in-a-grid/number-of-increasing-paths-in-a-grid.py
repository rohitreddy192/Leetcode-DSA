class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        if not grid: return 0
        
        MOD = 10**9 + 7

        @cache
        def dfs(r,c):
            cnt = 1
            dd = [[-1,0],[1,0],[0,-1],[0,1]]
            for dx, dy in dd:
                nr, nc = r+dx, c+dy
                if 0<=nr<n and 0<=nc<m and grid[nr][nc] > grid[r][c]:
                    cnt += dfs(nr,nc)
            
            return cnt%MOD

        
        return sum(dfs(r,c) for r in range(n) for c in range(m)) %MOD

        