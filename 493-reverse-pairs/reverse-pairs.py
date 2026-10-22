class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        
        def merge(l, m, h):
            i,j = l, m+1
            cnt = 0

            for i in range(l, m + 1):
                while j <= h and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += j - (m + 1)

            tmp = []
            i, j = l, m+1
            while i<=m and j<=h:
                if nums[i]<nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
            
            while i<=m:
                tmp.append(nums[i])
                i += 1
            
            while j<=h:
                tmp.append(nums[j])
                j += 1
            nums[l:h+1] = tmp
            return cnt
            

        def mergeSort(l,h):
            if l>=h: return 0
            cnt = 0
            m = (l+h)//2
            cnt += mergeSort(l, m)
            cnt += mergeSort(m+1,h)
            cnt += merge(l,m,h)
            return cnt

        l, h = 0, len(nums)-1
        return mergeSort(l,h)