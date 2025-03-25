class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # Function to get the maximum subarray of length `size` from `nums`
        def getMaxSubarray(nums, size):
            stack = []
            drop = len(nums) - size  # Number of elements we can drop
            for num in nums:
                while stack and drop and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:size]  # Return only the required size

        # Function to merge two subsequences into the largest lexicographical order
        def merge(arr1, arr2):
            res = []
            i, j = 0, 0
            while i < len(arr1) or j < len(arr2):
                if arr1[i:] > arr2[j:]:  # Lexicographical order comparison
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1
            return res
        
        max_result = []
        
        # Try all possible ways to split k elements between nums1 and nums2
        for x in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            sub1 = getMaxSubarray(nums1, x)  # Best x elements from nums1
            sub2 = getMaxSubarray(nums2, k - x)  # Best (k-x) elements from nums2
            max_result = max(max_result, merge(sub1, sub2))  # Pick the lexicographically largest
        
        return max_result