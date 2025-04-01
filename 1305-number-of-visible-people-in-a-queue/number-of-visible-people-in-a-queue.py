from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []  # Monotonic decreasing stack
        res = [0] * n  # Result array
        
        for i in range(n - 1, -1, -1):  # Traverse from right to left
            count = 0
            while stack and stack[-1] < heights[i]:  
                stack.pop()
                count += 1
            
            if stack:
                count += 1  # The next taller person is also visible
            
            res[i] = count
            stack.append(heights[i])  # Push current person to stack
        
        return res
