class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(i):
            if i<0: return 0
            if i==0: return nums[0]
            pick = nums[i] + solve(i-2)
            not_pick = solve(i-1)
            return max(pick,not_pick)

        n = len(nums)
        dp = [-1]*(n)
        dp[0] = nums[0]
        if n == 1: return nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            pick = nums[i] + dp[i-2]
            not_pick = dp[i-1]
            dp[i] = max(pick,not_pick)
        return dp[n-1]