class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        total = sum(nums)

        if total < 2 * k:
            return 0

        dp = [0] * k
        dp[0] = 1

        for num in nums:
            for s in range(k - 1, num - 1, -1):
                dp[s] = (dp[s] + dp[s - num]) % MOD

        bad = sum(dp) % MOD

        return (pow(2, len(nums), MOD) - 2 * bad) % MOD