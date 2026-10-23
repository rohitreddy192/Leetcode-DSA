class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum = 0
        prefix_sum = {}
        maxi = 0
        for jdx, num in enumerate(nums):
            sum += (-1 if num==0 else num)
            if sum == 0:
                maxi = jdx+1
            if sum in prefix_sum:
                maxi = max(maxi, jdx-prefix_sum[sum])
            else:
                prefix_sum[sum] = jdx
        
        return maxi