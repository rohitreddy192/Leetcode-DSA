class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        i = 0
        while i<n-2:
            if i>0 and nums[i]==nums[i-1]:
                i += 1
                continue
            j, k = i+1, n-1
            target = -1 * nums[i]
            while j<k:
                if nums[j]+nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    
                    while j<k and nums[j]==nums[j-1]:
                        j += 1

                    while j<k and nums[k]==nums[k+1]:
                        k -= 1
                elif nums[j]+nums[k] < target:
                    j += 1
                    while j<k and nums[j]==nums[j-1]:
                        j += 1
                else:
                    k -= 1
                    while j<k and nums[k]==nums[k+1]:
                        k -= 1
            
            i += 1
        return res