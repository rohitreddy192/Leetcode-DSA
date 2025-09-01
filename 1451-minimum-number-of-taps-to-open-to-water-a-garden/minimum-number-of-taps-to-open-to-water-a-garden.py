from functools import lru_cache
from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i, r in enumerate(ranges):
            start = max(0, i - r)
            end = min(n, i + r)
            intervals.append((start, end))
        
        @lru_cache(None)
        def dfs(pos: int) -> int:
            # Base case: if we already cover n
            if pos >= n:
                return 0  # no more taps needed
            
            ans = float("inf")
            for start, end in intervals:
                if start <= pos < end:  
                    # This tap can help extend coverage
                    ans = min(ans, 1 + dfs(end))
            
            return ans
        
        res = dfs(0)
        return -1 if res == float("inf") else res
