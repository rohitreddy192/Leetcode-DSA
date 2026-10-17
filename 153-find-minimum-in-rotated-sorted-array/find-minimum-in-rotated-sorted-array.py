class Solution:
    def findMin(self, nums: list[int]) -> int:
        low, high = 0, len(nums)-1
        ans = float("inf")
        while low<=high:
            mid = (low+high)//2
            if nums[mid]<nums[high]:
                ans = min(ans, nums[mid])
                high = mid-1

            else:
                ans = min(nums[low],ans)
                low = mid+1
        return ans
            






















    #     class Solution:
    # def findMin(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     low, high = 0, n-1
    #     while low<high:
    #         mid = (low+high)//2
    #         if nums[mid]>nums[high]:
    #             low = mid+1
    #         else:
    #             high = mid

    #     return nums[low]