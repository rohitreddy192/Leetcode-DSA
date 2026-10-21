
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)

        for i in range(n + 1):
            currHeight = heights[i] if i < n else 0

            while stack and heights[stack[-1]] > currHeight:
                height = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1

                maxArea = max(maxArea, height * width)

            stack.append(i)

        return maxArea
