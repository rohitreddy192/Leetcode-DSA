class Solution:
    def jump(self, nums: List[int]) -> int:  
        @lru_cache(None)
        def solve(i):
            if i>=len(nums)-1:
                return 0

            if nums[i]==0: return float("inf")
            
            tmp = float("inf")
            for j in range(1,nums[i]+1):
                tmp = min(tmp, 1 + solve(i+j))
            
            return tmp

        return solve(0)


        