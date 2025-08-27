class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        totalFreshOranges = 0
        dq = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    totalFreshOranges += 1
                if grid[i][j] == 2:
                    dq.append((i,j,0))
        time = 0
        nr = [-1,0,1,0]
        nc = [0,-1,0,1]
        while dq:
            x, y, t = dq.popleft()
            for i in range(4):
                nrow, ncol = nr[i]+x, nc[i]+y
                if 0<=nrow<n and 0<=ncol<m and grid[nrow][ncol] == 1:
                    dq.append((nrow, ncol, t+1))
                    grid[nrow][ncol] = 2
                    totalFreshOranges -= 1
                    time = max(time, t+1)
        
        if totalFreshOranges>0: return -1
        return time
