class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        ans = [[0 for _ in range(m)] for _ in range(n)]

        vis = defaultdict(set)
        dq = deque()
        houses = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dq.append((i, j, i, j, 0))
                    houses.add((i,j))
                    vis[(i,j)].add((i,j))

        while dq:
            sfx, sfy, x, y, d = dq.popleft()
            dx, dy = [-1,0,1,0], [0,-1,0,1]
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]==0 and (sfx,sfy) not in vis[(nx,ny)]:
                    vis[(nx,ny)].add((sfx,sfy))
                    dq.append((sfx,sfy,nx,ny,d+1))
                    ans[nx][ny] += d+1

        min_dist = float("inf")
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    if len(vis[(i,j)]) == len(houses):
                        min_dist = min(min_dist, ans[i][j])
        
        return -1 if min_dist == float("inf") else min_dist