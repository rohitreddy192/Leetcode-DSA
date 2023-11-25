class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = localMax =nums[0]
        for i in range(1,len(nums)):
            localMax = max(localMax+nums[i], nums[i])
            globalMax = max(globalMax,localMax)
        return globalMax