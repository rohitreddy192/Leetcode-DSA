class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n<=1: return nums
        dp = [0]*n
        maxi = 1
        prev = {i:i for i in range(n)}
        lastIndex = 0
        nums.sort()
        for i in range(n):
            dp[i] = 1
            for j in range(i):
                if nums[j]!=0 and nums[i]%nums[j]==0 and dp[i]<dp[j]+1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            if maxi<dp[i]:
                maxi = dp[i]
                lastIndex = i
        result = []
        result.append(nums[lastIndex])
        while lastIndex!=prev[lastIndex]:
            lastIndex = prev[lastIndex]
            result.append(nums[lastIndex])
        return result