class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        dq = deque()
        cnt = 0
        tot = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    dq.append((i,j,0))
                    cnt += 1
                    tot += 1
                if grid[i][j] == 1:
                    tot += 1
        
        max_t = 0
        while dq:
            for _ in range(len(dq)):
                x, y, t = dq.popleft()
                max_t = max(max_t, t)
                dx, dy = [-1,0,1,0], [0,-1,0,1]
                for di in range(4):
                    nx, ny = x+dx[di], y+dy[di]
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        dq.append((nx,ny, t+1))
                        cnt += 1
        
        if cnt==tot: return max_t
        return -1
        
