from typing import List

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        memo = {}
        houses.sort()
        return self.dfs(houses, 0, k, memo)

    def dfs(self, nums, i, k, memo):
        if (i, k) in memo:
            return memo[(i, k)]

        n = len(nums)

        if i == n and k == 0:
            return 0

        if i == n or k == 0:
            return float('inf')

        res = float('inf')

        for j in range(i, n):
            res = min(
                res,
                self.dfs(nums, j + 1, k - 1, memo)
                + self.cost(nums, i, j)
            )

        memo[(i, k)] = res
        return res

    def cost(self, nums, i, j):
        mid = (i + j) // 2
        res = 0

        for idx in range(i, j + 1):
            res += abs(nums[idx] - nums[mid])

        return res