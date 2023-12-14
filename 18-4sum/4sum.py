class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        i = 0
        while i<n:
            j = i+1
            while j<n:
                low = j + 1 
                high = n - 1
                new_target = target - nums[i] - nums[j]
                while low<high:
                    if new_target>(nums[low]+nums[high]):
                        low += 1
                    elif new_target<(nums[low]+nums[high]):
                        high -= 1
                    else:
                        quad1 = nums[i]
                        quad2 = nums[j]
                        quad3 = nums[low]
                        quad4 = nums[high]
                        res.append([quad1,quad2,quad3,quad4])
                        while low<high and nums[low] == quad3:
                            low += 1
                        while low<high and nums[high]==quad4:
                            high -= 1
                while j<n-1 and nums[j]==nums[j+1]:
                    j += 1
                j += 1
            while i<n-1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res