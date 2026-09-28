class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2 == 0:
                min_even = min(min_even, x)
            else:
                min_odd = min(min_odd, x)

        # Already uniform
        if min_odd == float('inf') or min_even == float('inf'):
            return True

        # Make everything odd
        return min_odd < min_even