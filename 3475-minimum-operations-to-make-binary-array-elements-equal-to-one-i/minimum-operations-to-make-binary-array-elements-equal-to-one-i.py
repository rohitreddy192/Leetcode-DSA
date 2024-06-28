class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1 if 0 in nums else 0
        op = 0
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1 - nums[i]
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                op += 1
        if any(num == 0 for num in nums):
            return -1
        
        return op