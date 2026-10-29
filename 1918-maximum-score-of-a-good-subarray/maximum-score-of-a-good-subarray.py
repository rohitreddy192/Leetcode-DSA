class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = right = k
        curr_min = nums[k]
        maxi = curr_min

        while left > 0 or right < n - 1:
            if left == 0:
                right += 1
            elif right == n - 1:
                left -= 1
            elif nums[left - 1] > nums[right + 1]:
                left -= 1
            else:
                right += 1

            curr_min = min(curr_min, nums[left], nums[right])
            maxi = max(maxi, curr_min * (right - left + 1))

        return maxi