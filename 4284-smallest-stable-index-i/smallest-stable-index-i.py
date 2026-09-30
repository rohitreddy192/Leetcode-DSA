class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefixMax = nums[:]
        suffixMin = nums[:]
        n = len(nums)
        for i in range(1,n):
            prefixMax[i] = max(prefixMax[i],prefixMax[i-1])
        
        for i in range(n-2,-1,-1):
            suffixMin[i] = min(suffixMin[i],suffixMin[i+1])

        for i in range(n):
            if prefixMax[i]-suffixMin[i] <= k:
                return i
        
        return -1