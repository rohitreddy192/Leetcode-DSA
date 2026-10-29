class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        m = max(nums)
        if m<0: return 1
        for i in range(1,m+1):
            if i not in s: return i

        return m+1

        # n = len(nums)
        # i = 0
        # while i<n:
        #     idx = nums[i] - 1
        #     if 0<nums[i]<=n and nums[i]!=nums[idx]:
        #         nums[i], nums[idx] = nums[idx], nums[i]
        #     else:
        #         i += 1
        
        # for i in range(n):
        #     if nums[i]!=i+1:
        #         return i+1
        
        # return n+1