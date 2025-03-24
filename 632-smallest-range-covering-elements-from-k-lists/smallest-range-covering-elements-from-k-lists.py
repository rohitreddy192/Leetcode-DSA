from heapq import heappush, heappop
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)  # Number of lists
        left, right = nums[0][0], nums[0][0]  # Initial range
        min_heap = []  # Min-heap to track the smallest element

        # Initialize the heap with the first element of each list
        for i in range(k):
            l = nums[i]
            left = min(left, l[0])
            right = max(right, l[0])
            heappush(min_heap, (l[0], i, 0))  # (value, list index, index in list)

        res = [left, right]

        while True:
            # Extract the smallest element from the heap
            n, i, idx = heappop(min_heap)
            idx += 1  # Move to the next element in the same list

            # If the list is exhausted, return the current best range
            if idx == len(nums[i]):
                return res

            next_val = nums[i][idx]  # Next element in the same list
            heappush(min_heap, (next_val, i, idx))  # Push next element into the heap

            right = max(right, next_val)  # Update the right boundary
            left = min_heap[0][0]  # The smallest value in the heap is the new left boundary

            # Update the result if the new range is smaller
            if right - left < res[1] - res[0]:
                res = [left, right]
