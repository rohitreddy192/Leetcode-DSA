from collections import deque

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS to track the time fire reaches each cell
        def bfsToTrackFire():
            fire_time = [[float('inf')] * COLS for _ in range(ROWS)]
            queue = deque()

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1:  # fire
                        queue.append((r, c, 0))
                        fire_time[r][c] = 0

            while queue:
                x, y, t = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == 0 and fire_time[nx][ny] == float('inf'):
                        fire_time[nx][ny] = t + 1
                        queue.append((nx, ny, t + 1))
            return fire_time

        # BFS to check if person can reach exit with given wait time
        def canEscapeWithWait(wait_time, fire_time):
            visited = [[False] * COLS for _ in range(ROWS)]
            queue = deque([(0, 0, wait_time)])

            while queue:
                x, y, t = queue.popleft()
                if (x, y) == (ROWS - 1, COLS - 1):
                    # If we reach destination before or at same time as fire
                    return t <= fire_time[x][y]

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < ROWS and 0 <= ny < COLS and not visited[nx][ny] and grid[nx][ny] == 0:
                        if t + 1 < fire_time[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny, t + 1))
                        elif (nx, ny) == (ROWS - 1, COLS - 1) and t + 1 == fire_time[nx][ny]:
                            # You can stand with fire at exit at same time
                            visited[nx][ny] = True
                            queue.append((nx, ny, t + 1))
            return False

        fire_time = bfsToTrackFire()

        if fire_time[0][0] == 0:
            return -1  # fire at the start

        left, right = 0, ROWS * COLS + 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            if canEscapeWithWait(mid, fire_time):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return 10**9 if answer >= ROWS * COLS else answer
