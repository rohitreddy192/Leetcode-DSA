
import heapq

class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])

        hp = [(0, (0, 0, k))]
        vis = {(0, 0, k)}

        while hp:
            dist, (x, y, rem) = heapq.heappop(hp)

            if (x, y) == (n - 1, m - 1):
                return dist

            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr, nc = x + dr, y + dc

                if not (0 <= nr < n and 0 <= nc < m):
                    continue

                new_k = rem - grid[nr][nc]

                if new_k < 0:
                    continue

                state = (nr, nc, new_k)

                if state not in vis:
                    vis.add(state)
                    heapq.heappush(
                        hp, (dist + 1, state)
                    )

        return -1
