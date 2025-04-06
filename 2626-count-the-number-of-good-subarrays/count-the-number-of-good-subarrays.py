class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        i = 0
        total_pairs = 0
        ans = 0
        
        for j in range(n):
            # Add nums[j] into window
            total_pairs += d[nums[j]]
            d[nums[j]] += 1

            # Shrink window from left if pairs >= k
            while total_pairs >= k:
                # All subarrays starting from i to end are valid
                ans += (n - j)
                d[nums[i]] -= 1
                total_pairs -= d[nums[i]]
                i += 1

        return ans