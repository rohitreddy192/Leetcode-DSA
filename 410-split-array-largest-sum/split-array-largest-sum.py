class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        def isPossible(mid):
            splits = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num > mid:
                    splits += 1
                    curr_sum = num
                else:
                    curr_sum += num

            return splits <= k

        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low + high) // 2

            if isPossible(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low