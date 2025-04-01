class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        mpp = {}
        n, m = len(grid), len(grid[0])
        for q in queries:
            mpp[q] = 0
        
        sort_q = sorted(queries)
        
        cnt = 0
        vis = set()
        hp = []
        heapq.heappush(hp, (grid[0][0],0,0))
        vis.add((0,0))
        
        for i in sort_q:
            while hp:
                val, x, y = hp[0]
                if val<i:
                    heapq.heappop(hp)
                    cnt += 1
                    for dx, dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<n and 0<=ny<m and (nx,ny) not in vis:
                            heapq.heappush(hp, (grid[nx][ny],nx,ny))
                            vis.add((nx,ny))
                else:
                    break
            
            mpp[i] = cnt
        
        res = []
        for q in queries:
            res.append(mpp[q])
        
        return res
