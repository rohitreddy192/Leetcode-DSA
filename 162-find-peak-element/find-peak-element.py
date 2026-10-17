class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        if nums[-1] > nums[-2]:
            return n - 1
        if nums[0] > nums[1]:
            return 0

        l, h = 1, n - 2

        while l <= h:
            m = (l + h) // 2

            if nums[m] > nums[m+1] and nums[m] > nums[m-1]:
                return m
            elif nums[m] < nums[m+1]:
                l = m + 1
            else:
                h = m - 1

        return l