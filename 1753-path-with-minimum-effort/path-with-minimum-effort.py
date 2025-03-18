import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        # Distance array to track min effort to reach each cell
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        
        hp = [(0, 0, 0)]  # Min-heap: (effort, row, col)

        while hp:
            effort, x, y = heapq.heappop(hp)
            
            # If we reach the destination, return the effort
            if x == n - 1 and y == m - 1:
                return effort
            
            for i in range(4):
                nrow, ncol = x + dx[i], y + dy[i]
                
                if 0 <= nrow < n and 0 <= ncol < m:
                    new_effort = max(effort, abs(heights[nrow][ncol] - heights[x][y]))
                    
                    if new_effort < dist[nrow][ncol]:  # Only push if we find a better path
                        dist[nrow][ncol] = new_effort
                        heapq.heappush(hp, (new_effort, nrow, ncol))

        return -1
