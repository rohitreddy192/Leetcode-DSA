class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        hp = []
        dist = defaultdict(lambda: float("inf"))
        heapq.heappush(hp, (1,0,0))
        dist[(0,0)] = 1
        if grid[0][0]==1 or grid[n-1][m-1]==1: return -1

        while hp:
            dist_, x, y = heapq.heappop(hp)

            if (x,y) == (n-1,m-1):
                return dist_
                
            directions = [
                (-1,-1), (-1,0), (-1,1),
                (0,-1),          (0,1),
                (1,-1),  (1,0),  (1,1)
            ]
            for dx,dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]==0:
                    if dist[(nx,ny)] > dist_+1:
                        dist[(nx,ny)] = dist_+1
                        heapq.heappush(hp,(dist[(nx,ny)],nx,ny))

        return -1