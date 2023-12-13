class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(low,mid,high):
            temp = []
            i,j = low, mid+1
            inv = 0
            for i in range(low,mid+1):
                while j<=high and nums[i]>2*nums[j]:
                    j += 1
                inv += (j-mid-1)
        


            i,j  = low,mid+1

            while i<=mid and j<=high:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i<=mid:
                temp.append(nums[i])
                i += 1
            while j<=high:
                temp.append(nums[j])
                j += 1
            for i in range(low,high+1):
                nums[i] = temp[i-low]
            return inv

        def mergeSort(low,high):
            inv = 0
            if low>=high: return inv
            mid = (low+high)//2
            inv += mergeSort(low,mid)
            inv += mergeSort(mid+1,high)
            inv += merge(low,mid,high)
            return inv
        
        return mergeSort(0,len(nums)-1)