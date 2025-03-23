class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0  # Need at least 3 elements

        # Memoization dictionary (index, difference) → count
        dp = [defaultdict(int) for _ in range(n)]
        total_count = 0
        
        # Recursion with memoization
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count_at_j = dp[j][diff]
                dp[i][diff] += count_at_j + 1
                total_count += count_at_j  # Only count subsequences of length >= 3

        return total_count
