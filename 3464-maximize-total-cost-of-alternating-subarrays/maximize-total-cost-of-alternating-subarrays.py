class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        @cache
        def dp(x):
            if x >= len(nums):
                return 0
            
            ans = nums[x] + dp(x + 1)
            if x < len(nums) - 1:
                ans = max(ans, nums[x] - nums[x + 1] + dp(x + 2))
            return ans
        return dp(0)    