class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        vis = set()
        def dfs(vis, i, j):
            vis.add((i,j))
            dx, dy = [-1,0,1,0],[0,-1,0,1]
            for di in range(4):
                nx, ny = i+dx[di], j+dy[di]
                if 0<=nx<n and 0<=ny<m and (nx,ny) not in vis and grid[nx][ny]=="1":
                    dfs(vis,nx,ny)
        
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and (i,j) not in vis:
                    cnt += 1
                    dfs(vis,i,j)
        
        return cnt