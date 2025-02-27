class Solution:
    def trap(self,heights):
        n = len(heights)
        if n == 0:
            return 0
        
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = heights[0]
        suffix[n - 1] = heights[n - 1]
        
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], heights[i])
        
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], heights[i])
        
        ans = 0
        for i in range(n):
            ans += min(prefix[i], suffix[i]) - heights[i]
        
        return ans