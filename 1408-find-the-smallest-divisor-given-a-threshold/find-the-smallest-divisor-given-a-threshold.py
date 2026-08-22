class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def isPossible(k):
            total = 0

            for num in nums:
                total += math.ceil(num / k)

            return total <= threshold

        low, high = 1, max(nums)

        while low < high:
            mid = (low + high) // 2

            if isPossible(mid):
                high = mid
            else:
                low = mid + 1

        return low