from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        m, n = len(rooms[0]), len(rooms)

        ans = [row[:] for row in rooms]
        vis = set()
        dq = deque()

        # Add all gates
        for i in range(n):
            for j in range(m):

                if rooms[i][j] == 0:
                    dq.append((i, j, 0))
                    ans[i][j] = 0
                    vis.add((i, j))

        # BFS
        while dq:

            x, y, t = dq.popleft()

            dx = [-1, 0, 1, 0]
            dy = [0, -1, 0, 1]

            for i in range(4):

                nx = x + dx[i]
                ny = y + dy[i]

                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and rooms[nx][ny] != -1
                    and (nx, ny) not in vis
                ):
                    dq.append((nx, ny, t + 1))
                    vis.add((nx, ny))
                    ans[nx][ny] = t + 1

        # Copy result back
        for i in range(n):
            for j in range(m):
                rooms[i][j] = ans[i][j]