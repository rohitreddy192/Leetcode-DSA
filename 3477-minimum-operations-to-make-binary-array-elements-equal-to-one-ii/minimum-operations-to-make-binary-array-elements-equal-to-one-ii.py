class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        op = 0
        f = False  
        for i in range(n):
            if nums[i] == f:
                op += 1
                f = not f  
        return op