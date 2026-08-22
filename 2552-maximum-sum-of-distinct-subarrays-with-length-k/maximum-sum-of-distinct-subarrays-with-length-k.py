class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        curr_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            # Add current element
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            curr_sum += nums[right]

            # If duplicate exists, shrink window
            while freq[nums[right]] > 1:
                freq[nums[left]] -= 1
                curr_sum -= nums[left]
                left += 1

            # Keep window size <= k
            if right - left + 1 > k:
                freq[nums[left]] -= 1
                curr_sum -= nums[left]
                left += 1

            # Valid window of exactly k distinct elements
            if right - left + 1 == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum