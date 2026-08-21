class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat[0]), len(mat)
        dist = [[-1 for _ in range(m)] for _ in range(n) ]

        dq = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    dq.append((i,j))
                    dist[i][j] = 0


        while dq:
            x,y = dq.popleft()
            dx, dy = [-1,0,1,0],[0,-1,0,1]
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<m and dist[nx][ny]==-1:
                    dist[nx][ny] = dist[x][y] + 1
                    dq.append((nx,ny))
        
        return dist