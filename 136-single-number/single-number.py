class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        reVal = nums[0]
        for num in nums[1:]:
            reVal ^= num
        
        return reVal