class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid[0]), len(grid)

        vis = {}
        dq = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "*":
                    dq.append((i, j, 0))
                    vis[(i, j)] = True

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        while dq:
            x, y, t = dq.popleft()
            if grid[x][y]=="#":
                return t

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and (nx, ny) not in vis
                    and grid[nx][ny] in ["O", "#"]
                ):
                    dq.append((nx, ny, t + 1))
                    vis[(nx, ny)] = True

        return -1