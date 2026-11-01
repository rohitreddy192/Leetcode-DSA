
class Solution:
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        bits = [0] * 31

        # Count frequency of each set bit
        for num in nums:
            for b in range(31):
                if num & (1 << b):
                    bits[b] += 1

        ans = 0

        # Construct k maximum numbers greedily
        for _ in range(k):
            curr = 0

            for b in range(31):
                if bits[b] > 0:
                    curr |= (1 << b)
                    bits[b] -= 1

            ans = (ans + curr * curr) % MOD

        return ans
