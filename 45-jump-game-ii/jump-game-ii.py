class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r  = 0, 0
        n = len(nums)
        res = 0
        while r<n-1:
            far = 0
            for j in range(l,r+1):
                far = max(far, j + nums[j])
            
            l = r + 1
            r = far
            res += 1
        
        return res