class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        # if len(nums)<2: return nums[0]
        # if not nums: return -1
        ans = float("inf")
        while low<=high:
            mid = (low+high)//2
            if low!=mid!=high and nums[low]==nums[mid]==nums[high]:
                low += 1
                high -= 1
                ans = min(ans, nums[mid])
                continue
            elif nums[mid]<=nums[high]:
                ans = min(ans, nums[mid])
                high = mid-1

            else:
                ans = min(nums[low],ans)
                low = mid+1
        
        return ans