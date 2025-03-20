from typing import List

class DisJointSet:
    
    def __init__(self, n, m):
        self.parent = [[(i, j) for j in range(m)] for i in range(n)]
        self.size = [[1 for _ in range(m)] for _ in range(n)]

    def findUPar(self, x, y):
        if self.parent[x][y] != (x, y):  # Not the root
            self.parent[x][y] = self.findUPar(*self.parent[x][y])  # Path compression
        return self.parent[x][y]

    def unionBySize(self, x1, y1, x2, y2):
        root1X, root1Y = self.findUPar(x1, y1)
        root2X, root2Y = self.findUPar(x2, y2)

        if (root1X, root1Y) == (root2X, root2Y):  # Already in the same set
            return False  # No change in the number of islands
        
        # Attach smaller tree to larger tree
        if self.size[root1X][root1Y] < self.size[root2X][root2Y]:
            self.parent[root1X][root1Y] = (root2X, root2Y)
            self.size[root2X][root2Y] += self.size[root1X][root1Y]
        else:
            self.parent[root2X][root2Y] = (root1X, root1Y)
            self.size[root1X][root1Y] += self.size[root2X][root2Y]

        return True  # Islands merged

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ds = DisJointSet(m, n)
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        island_count = 0
        result = []

        for queryX, queryY in positions:
            if grid[queryX][queryY] == 1:  # Ignore duplicate land addition
                result.append(island_count)
                continue

            grid[queryX][queryY] = 1
            island_count += 1  # New land, increase island count

            for i in range(4):  # Check 4 neighbors
                nrow, ncol = queryX + dx[i], queryY + dy[i]
                if 0 <= nrow < m and 0 <= ncol < n and grid[nrow][ncol] == 1:
                    if ds.unionBySize(nrow, ncol, queryX, queryY):  # Merging islands
                        island_count -= 1

            result.append(island_count)

        return result
