class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Same as 2Sum => nums[i]+nums[j] = -1*nums[k] ===> target=(-1*nums[k])
        Loop in for target and then do 2Sum.
        """
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            target = -1* nums[i]
            low, high = i+1, n-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while low<high:
                add_n = nums[low]+nums[high]
                if add_n == target:
                    result.append([nums[i], nums[low],nums[high]])
                    while low<high and nums[low]==nums[low+1]:
                        low += 1
                    while low<high and nums[high]==nums[high-1]:
                        high -= 1
                    
                    low += 1
                    high -= 1

                elif add_n>target:
                    high -= 1
                else:
                    low += 1
        return result
