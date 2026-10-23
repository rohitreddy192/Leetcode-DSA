class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row, col = 0, 0
        if not matrix: return False
        n,m = len(matrix), len(matrix[0])
        dq = deque()
        dq.append((row,col))
        if matrix[row][col]==target: return True

        vis = set()
        while dq:
            row, col = dq.popleft()
            dd = [[-1,0],[1,0],[0,-1],[0,1]]
            for dx, dy in dd:
                nr, nc = row+dx, col+dy
                if 0<=nr<n and 0<=nc<m and (nr,nc) not in vis:
                    if matrix[nr][nc]>target:
                        vis.add((nr,nc))
                        continue
                    
                    if matrix[nr][nc]<=target:
                        if matrix[nr][nc]==target: return True
                        vis.add((nr,nc))
                        dq.append((nr,nc))
        
        return False