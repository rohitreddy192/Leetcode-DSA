from typing import List
from functools import lru_cache

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n = len(words[0])  # Number of columns
        m = len(target)  # Length of target
        
        # Step 1: Precompute frequency of each character in each column
        freq = [[0] * 26 for _ in range(n)]
        for word in words:
            for i, ch in enumerate(word):
                freq[i][ord(ch) - ord('a')] += 1
        
        # Step 2: Memoized DFS to count ways
        @lru_cache(None)
        def solve(i, j):
            if j == m:  # Successfully formed the target
                return 1
            if i == n:  # Exhausted all columns
                return 0
            
            # Option 1: Skip this column
            res = solve(i + 1, j)  
            
            # Option 2: Use this column if possible
            char_index = ord(target[j]) - ord('a')
            if freq[i][char_index] > 0:
                res = (res + freq[i][char_index] * solve(i + 1, j + 1)) % MOD
            
            return res

        return solve(0, 0)
