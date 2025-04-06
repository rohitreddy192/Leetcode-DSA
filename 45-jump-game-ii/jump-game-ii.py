class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        @lru_cache(None)
        def solve(i):
            if i>=n-1:
                return 0
            
            pick = 1e9
            for j in range(1,nums[i]+1):
                pick = min(pick, 1 + solve(i+j))

            return pick
        
        return solve(0)