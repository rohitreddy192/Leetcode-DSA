class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hm = {}
        for idx, num in enumerate(nums):
            if num in hm:
                if idx - hm[num] <= k:
                    return True
            hm[num] = idx
        return False