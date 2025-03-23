class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0  # Need at least 3 elements

        count = 0  # Tracks arithmetic subarrays ending at the current index
        total_slices = 0  # Final count

        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                count += 1  # Extend the previous arithmetic subarray
                total_slices += count  # Add count to total
            else:
                count = 0  # Reset count if the pattern breaks

        return total_slices