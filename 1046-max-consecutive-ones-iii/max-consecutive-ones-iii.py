class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i,j = 0, 0
        tmp = k
        maxi = 0
        while j<n:
            while nums[j]==0 and tmp<=0:
                if nums[i]==0:
                    tmp += 1
                i += 1

            if nums[j]==0 and tmp>0:
                tmp -= 1

            j += 1

            maxi = max(maxi, j-i)
        return maxi