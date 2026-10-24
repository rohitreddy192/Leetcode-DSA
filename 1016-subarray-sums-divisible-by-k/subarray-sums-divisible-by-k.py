class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        sum = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        cnt = 0
        for idx, num in enumerate(nums):
            sum += num
            cnt += prefix_sum[sum%k]
            prefix_sum[sum%k] += 1
        
        return cnt