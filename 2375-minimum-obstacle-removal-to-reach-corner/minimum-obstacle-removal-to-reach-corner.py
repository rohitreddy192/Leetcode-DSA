class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up
        
        # Min-Heap stores (obstacles_removed, x, y)
        heap = [(0, 0, 0)]  # Start from (0,0) with 0 obstacles removed
        visited = [[float('inf')] * n for _ in range(m)]  # Stores min obstacles needed to reach (i,j)
        visited[0][0] = 0  # Start cell requires no removal
        
        while heap:
            obstacles_removed, x, y = heapq.heappop(heap)
            
            # If reached destination, return the answer
            if x == m-1 and y == n-1:
                return obstacles_removed
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:  # Ensure within bounds
                    new_obstacles = obstacles_removed + grid[nx][ny]  # Remove obstacle if present
                    
                    # If we found a better way to reach (nx, ny), update and push
                    if new_obstacles < visited[nx][ny]:
                        visited[nx][ny] = new_obstacles
                        heapq.heappush(heap, (new_obstacles, nx, ny))
        
        return -1  # Should never reach here
