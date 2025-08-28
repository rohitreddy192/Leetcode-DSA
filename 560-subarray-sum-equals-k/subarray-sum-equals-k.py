from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        sum_ = 0
        mpp = defaultdict(int)
        mpp[0] = 1
        cnt = 0

        for num in nums:
            sum_ += num
            if (sum_ - k) in mpp:
                cnt += mpp[sum_ - k]
            mpp[sum_] += 1

        return cnt
