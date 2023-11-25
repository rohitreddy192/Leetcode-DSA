class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = mid = 0
        high = len(nums)-1
        while mid<=high:
            match nums[mid]:
                case 0:
                    nums[low], nums[mid] = nums[mid], nums[low]
                    low += 1
                    mid += 1
                case 1:
                    mid += 1
                case 2:
                    nums[high], nums[mid] = nums[mid], nums[high]
                    high -= 1
        