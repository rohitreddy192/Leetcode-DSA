from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        h = Counter(nums)
        count = 0

        if k == 0:
            for key in h:
                if h[key] > 1:
                    count += 1
            return count
        else:
            for key in h:
                if key + k in h:
                    count += 1
            return count
