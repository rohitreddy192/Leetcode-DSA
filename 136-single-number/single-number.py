class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = list(set(nums))
        sn = sum(nums)
        ss = sum(s)
        return ss*2 - sn