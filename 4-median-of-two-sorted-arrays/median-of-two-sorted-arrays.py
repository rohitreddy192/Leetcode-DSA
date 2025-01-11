from typing import List

class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        n, m = len(arr1), len(arr2)
        i, j = 0, 0
        merged_count = 0
        total_len = n + m
        median_pos = total_len // 2

        # Track current and previous elements
        prev, curr = None, None

        # Simulate merging until the median position is reached
        while merged_count <= median_pos:
            prev = curr  # Store the previous element
            
            # Choose the smaller element from the two arrays
            if i < n and (j >= m or arr1[i] < arr2[j]):
                curr = arr1[i]
                i += 1
            else:
                curr = arr2[j]
                j += 1

            merged_count += 1

        # Determine the median based on the total length
        if total_len % 2 == 0:  # Even length
            return (prev + curr) / 2
        else:  # Odd length
            return curr
