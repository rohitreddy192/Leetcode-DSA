class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
    
        @lru_cache(None)
        def dfs(i, j):
            # Base case: if we reach the bottom-right corner, the minimum health needed to survive
            # is max(1, 1 - dungeon[i][j])
            if i == m - 1 and j == n - 1:
                return max(1, 1 - dungeon[i][j])
            
            # Recursive case: move right or down, choosing the path with the minimum required health
            min_health = float('inf')
            if i + 1 < m:
                min_health = min(min_health, dfs(i + 1, j))
            if j + 1 < n:
                min_health = min(min_health, dfs(i, j + 1))
            
            # Calculate the health needed to enter this cell
            return max(1, min_health - dungeon[i][j])
        
        return dfs(0, 0)
