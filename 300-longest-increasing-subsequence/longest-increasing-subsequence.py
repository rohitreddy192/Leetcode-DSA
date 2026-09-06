class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(lambda :1)
        maxi = 1
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j] and 1 + dp[j]>dp[i]:
                    dp[i] = dp[j]+1
            maxi = max(maxi,dp[i])
        return maxi