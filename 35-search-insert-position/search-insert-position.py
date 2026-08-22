class Solution:
    def solve(self, arr, target, n):
        low, high = 0, n-1
        ans = n
        while low<=high:
            mid = (low+high)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.solve(nums,target, len(nums))


"""
1,3,5,6 => 2

low = 0
high = 3

mid = 1
3>2 => high = mid
       ans = mid


"""