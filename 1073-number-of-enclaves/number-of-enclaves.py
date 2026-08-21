class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dq = deque()
        n, m = len(grid), len(grid[0])
        for i in range(n):
            if grid[i][0] == 1:
                dq.append([i,0])
                grid[i][0] = 0
            if grid[i][m-1] == 1:
                dq.append([i,m-1])
                grid[i][m-1] = 0
        for j in range(m):
            if grid[0][j] == 1:
                dq.append([0,j])
                grid[0][j] = 0
            if grid[n-1][j] == 1:
                dq.append([n-1,j])
                grid[n-1][j] = 0
        
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        while dq:
            x, y = dq.popleft()
            for i in range(4):
                drow = dx[i]+x
                dcol = dy[i]+y
                if 0<=drow<n and 0<=dcol<m and grid[drow][dcol]==1:
                    grid[drow][dcol] = 0
                    dq.append([drow,dcol])
        
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt += 1
        return cnt