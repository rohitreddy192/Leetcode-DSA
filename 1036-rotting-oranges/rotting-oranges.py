class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        
        # Initialize visited and fresh orange count
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))  # Initially rotten oranges
                elif grid[i][j] == 1:
                    fresh += 1  # Count fresh oranges
        
        if fresh == 0: return 0  # No fresh oranges to rot
        
        cnt = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # BFS process
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # Rot the fresh orange
                        q.append((nx, ny))
                        fresh -= 1  # Decrease the count of fresh oranges
            cnt += 1
        
        return cnt-1 if fresh == 0 else -1 