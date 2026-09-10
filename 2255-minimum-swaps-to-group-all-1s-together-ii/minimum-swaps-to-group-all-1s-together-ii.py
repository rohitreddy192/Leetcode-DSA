class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        windowSize = sum(nums)

        if windowSize <= 1 or windowSize == n:
            return 0

        windowSum = 0

        # First window
        for i in range(windowSize):
            windowSum += nums[i]

        maxSum = windowSum

        # Circular sliding window
        for r in range(windowSize, n + windowSize):
            windowSum -= nums[(r - windowSize) % n]
            windowSum += nums[r % n]

            maxSum = max(maxSum, windowSum)

        return windowSize - maxSum