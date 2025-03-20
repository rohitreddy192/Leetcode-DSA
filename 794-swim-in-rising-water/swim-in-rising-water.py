from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        # Min-heap to store (max elevation encountered so far, row, col)
        pq = [(grid[0][0], 0, 0)]  # (time, x, y)
        visited = set((0, 0))  # Mark starting position
        
        while pq:
            time, r, c = heappop(pq)  # Always expand the lowest time first
            
            # If we reached bottom-right, return the max elevation encountered
            if r == n - 1 and c == n - 1:
                return time
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # Push the max time required so far
                    heappush(pq, (max(time, grid[nr][nc]), nr, nc))
        
        return -1  # This should never be reached
