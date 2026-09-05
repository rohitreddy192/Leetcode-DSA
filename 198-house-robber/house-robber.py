class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = {}
        def solve(idx):
            if idx < 0: return 0
            if idx in dp: return dp[idx]

            pick = nums[idx] + solve(idx-2)
            not_pick = solve(idx-1)

            dp[idx] =  max(pick, not_pick)

            return dp[idx]
        
        return solve(len(nums)-1)