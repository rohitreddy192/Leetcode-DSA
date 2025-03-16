class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        freshCnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((0,(i,j)))
                if grid[i][j]==1:
                    freshCnt += 1
        maxi = 0
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        while q:
            time, node = q.popleft()
            x, y = node
            maxi = max(time,maxi)
            for i in range(4):
                nrow, ncol = x+dx[i], y+dy[i]
                if 0<=nrow<n and 0<=ncol<m and grid[nrow][ncol]==1:
                    grid[nrow][ncol]=2
                    freshCnt -= 1
                    q.append((time+1,(nrow,ncol)))
        
        print(grid)

        return maxi if freshCnt==0 else -1
            
