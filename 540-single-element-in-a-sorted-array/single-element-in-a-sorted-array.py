class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]
        if n==2: return -1
        low = 1
        high = n-2
        if nums[0]!=nums[1]: return nums[0]
        if nums[n-1]!=nums[n-2]: return nums[n-1]
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==nums[mid-1]:
                if mid%2 == 1:
                    low = mid+1
                else:
                    high = mid-1
            elif nums[mid]==nums[mid+1]:
                if mid%2==0:
                    low = mid+1
                else:
                    high = mid-1
            else:
                return nums[mid]
        return -1