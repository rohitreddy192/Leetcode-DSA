class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def merge(low, mid, high):
            # Count reverse pairs
            j = mid + 1
            cnt = 0

            for i in range(low, mid + 1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1

                cnt += j - (mid + 1)

            # Normal merge
            i = low
            j = mid + 1
            temp = []

            while i <= mid and j <= high:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= high:
                temp.append(nums[j])
                j += 1

            for k in range(low, high + 1):
                nums[k] = temp[k - low]

            return cnt

        def mergeSort(low, high):
            if low >= high:
                return 0

            mid = (low + high) // 2

            cnt = mergeSort(low, mid)
            cnt += mergeSort(mid + 1, high)
            cnt += merge(low, mid, high)

            return cnt

        return mergeSort(0,len(nums)-1)
            
            