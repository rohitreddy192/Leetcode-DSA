class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        sum = 0
        minLen = float("inf")
        while r<len(nums):
            sum += nums[r]
            while sum>=target:
                minLen = min(minLen,r-l+1)
                sum -= nums[l]
                l += 1
            r += 1
        return minLen if minLen<=len(nums) else 0