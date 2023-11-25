class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def swap(nums,i,j):
            nums[i], nums[j] = nums[j], nums[i]
        def reverse(nums,i,j):
            while(i<j):
                swap(nums,i,j)
                i += 1
                j -= 1
        ind = -1
        n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind = i
                break
        if ind==-1:
            reverse(nums,0,n-1)
            return nums
        for i in range(n-1,ind,-1):
            if nums[i]>nums[ind]:
                swap(nums,i,ind)
                reverse(nums,ind+1,n-1)
                return nums