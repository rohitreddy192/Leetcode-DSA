class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = set(nums)
        if len(x)<3:
            return max(x)
        x = sorted(x, reverse = True)
        return x[2]
        