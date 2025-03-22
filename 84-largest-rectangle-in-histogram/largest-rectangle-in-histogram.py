from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        # Next Smaller Element (NSE)
        def nse():
            stack = []
            res = [n] * n  # Default next smaller index is 'n' (out of bounds)
            for i in range(n - 1, -1, -1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    res[i] = stack[-1]
                stack.append(i)
            return res
        
        # Previous Smaller Element (PSE)
        def pse():
            stack = []
            res = [-1] * n  # Default previous smaller index is '-1' (out of bounds)
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    res[i] = stack[-1]
                stack.append(i)
            return res
        
        next_smaller = nse()
        prev_smaller = pse()

        max_area = 0
        for i in range(n):
            width = next_smaller[i] - prev_smaller[i] - 1
            max_area = max(max_area, heights[i] * width)
        
        return max_area
