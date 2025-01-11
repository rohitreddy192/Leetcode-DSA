class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start, end = 0, n-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid

            if nums[start]<=nums[mid]:
                if nums[start]<=target<nums[mid]:
                    end = mid
                else:
                    start = mid+1

            else:
                if nums[mid]<=target<=nums[end]:
                    start = mid
                else:
                    end = mid -1

        return -1
