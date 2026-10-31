class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])

        @cache
        def getMin(i,j):
            if i==n-1 and j==m-1:
                return 1 if dungeon[i][j]>=0 else -dungeon[i][j]+1

            best = float("inf")
            if i+1<n:
                minDown = getMin(i+1,j)
                best = min(best, 1 if dungeon[i][j]>=minDown else minDown - dungeon[i][j])
            if j+1<m:
                minRight = getMin(i,j+1)
                best = min(best, 1 if dungeon[i][j]>=minRight else minRight-dungeon[i][j])

            return best
        
        return getMin(0,0)