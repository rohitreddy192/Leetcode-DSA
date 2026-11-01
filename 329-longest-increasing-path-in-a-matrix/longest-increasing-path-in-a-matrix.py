class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix: 
            return 0

        n, m = len(matrix), len(matrix[0])

        @cache
        def dfs(r,c):
            max_length = 1
            dd = [[-1,0],[0,-1],[0,1],[1,0]]
            for dx, dy in dd:
                nr, nc = r+dx, c+dy
                if 0<=nr<n and 0<=nc<m and matrix[r][c]<matrix[nr][nc]:
                    max_length = max(max_length, 1 + dfs(nr,nc))

            return max_length

        return max(dfs(r,c) for r in range(n) for c in range(m))