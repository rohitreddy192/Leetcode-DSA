class Solution:
    def trap(self, heights: list[int]) -> int:
        prefix = heights[:]
        suffix = heights[:]
        
        n = len(heights)
        for i in range(1,n):
            prefix[i] = max(prefix[i-1], heights[i])
        for i in range(n-2,-1,-1):
            suffix[i] = max(suffix[i+1], heights[i])

        ans = 0
        for i in range(n):
            ans += (min(prefix[i], suffix[i]) - heights[i])
        
        return ans