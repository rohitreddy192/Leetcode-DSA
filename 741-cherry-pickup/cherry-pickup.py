class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        N = len(grid)

        @cache
        def solve(r1, c1, r2, c2):

            if r1>=N or r2>=N or c1>=N or c2>=N or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float("-inf")

            if r1==N-1 and c1==N-1:
                return grid[r1][c1]
            
            cherries = grid[r1][c1] if (r1,c1)==(r2,c2) else grid[r1][c1]+grid[r2][c2]

            cherries += max(
                solve(r1,c1+1, r2,c2+1),
                solve(r1+1, c1, r2+1, c2),
                solve(r1+1, c1, r2, c2+1),
                solve(r1, c1+1,r2+1, c2)
                )

            return cherries

                # down, right
                # A D B R
                # A R B D
                # A D B D 
                # A R B R 

        return max(0,solve(0,0,0,0))