
from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()
        ans = float("inf")

        for i in range(n + 1):

            # Rule 1: Found a valid subarray
            while dq and prefix[i] - prefix[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())

            # Rule 2: Remove dominated candidates
            while dq and prefix[dq[-1]] >= prefix[i]:
                dq.pop()

            dq.append(i)

        return ans if ans != float("inf") else -1
