class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 40,19, 12, 9
        def merge(low,mid,high):
            cnt = 0
            i = low
            j = mid+1
            temp = []
            for i in range(low,mid+1):
                while j<=high and nums[i]>2*nums[j]:
                    j += 1
                cnt += (j-mid-1)            
            i = low
            j = mid+1
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
            return cnt


        def merge_sort(low,high):
            cnt = 0
            if low<high:
                mid = (low+high)//2
                cnt += merge_sort(low,mid)
                cnt += merge_sort(mid+1,high)
                cnt += merge(low,mid,high)
            return cnt

        return merge_sort(0,len(nums)-1)