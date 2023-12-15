class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    dq.append([i,j])
        time = 0
        while dq:
            for i in range(len(dq)):
                x, y = dq.popleft()
                drow = [-1,0,1,0]
                dcol = [0,-1,0,1]
                for i in range(4):
                    dx, dy = drow[i]+x, dcol[i]+y
                    if dx>=0 and dx<n and dy>=0 and dy<m and grid[dx][dy]==1:
                        dq.append([dx,dy])
                        grid[dx][dy] = 2
            time += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return time-1 if time!=0 else 0