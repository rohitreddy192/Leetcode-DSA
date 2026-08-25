class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        n = len(nums)
        sum = nums[0]
        for i in range(1,n):
            sum = max(sum+nums[i], nums[i])
            maxSum = max(maxSum, sum)
        return maxSum