class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*(n)
        count = [1]*(n)

        for i in range(1,n):

            for j in range(i):

                if nums[i]>nums[j] and 1+dp[j]>dp[i]:
                    dp[i] = 1+dp[j]
                    count[i] = count[j]
                    
                elif nums[i]>nums[j] and 1+dp[j]==dp[i]:
                    count[i] += count[j]
        
        return sum(count[i] for i in range(n) if dp[i]==max(dp))