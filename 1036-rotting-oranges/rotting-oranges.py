class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m =len(grid), len(grid[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([0,i,j])
        maxi = 0
        while q:
            time, x, y = q.popleft()
            dx, dy = [-1,0,1,0], [0,-1,0,1]
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]==1:
                    q.append([time+1,nx,ny])
                    grid[nx][ny]=2
                    maxi = max(maxi, time+1)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return maxi