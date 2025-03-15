class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        maxi = 1
        count = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j] and 1+dp[j]>dp[i]:
                    dp[i] = 1 + dp[j]
                    count[i] = count[j]
                elif nums[i]>nums[j] and 1+dp[j]==dp[i]:
                    count[i] += count[j]
            if maxi<dp[i]:
                maxi = dp[i]
        cnt = 0
        for i in range(n):
            if dp[i] == maxi:
                cnt += count[i]
        return cnt