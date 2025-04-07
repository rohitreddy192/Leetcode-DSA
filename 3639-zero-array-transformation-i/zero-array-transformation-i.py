class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        sweep = [0] * (n + 1)

        for l, r in queries:
            sweep[l] += 1
            sweep[r + 1] -= 1

        for i in range(1, n + 1):
            sweep[i] += sweep[i - 1]

        return all(sweep[i] >= nums[i] for i in range(n))