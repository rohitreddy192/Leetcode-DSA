class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        low, mid, high = 0, 0, n-1

        while mid<=high:
            if nums[mid]==0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            
            elif nums[mid]==1:
                mid += 1

            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1

        
        return nums