class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        arr = [0]*(m+n)
        idx = 0
        while i<m and j<n and idx<(m+n):
            if nums1[i]<nums2[j]:
                arr[idx] = nums1[i]
                i += 1
            else:
                arr[idx] = nums2[j]
                j += 1

            idx += 1

        while idx<(m+n) and i<m:
            arr[idx] = nums1[i]
            i += 1
            idx += 1
        
        while idx<(m+n) and j<n:
            arr[idx] = nums2[j]
            j += 1
            idx += 1
        
        for i in range(m+n):
            nums1[i] = arr[i]
            