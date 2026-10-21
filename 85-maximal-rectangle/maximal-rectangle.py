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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        maxArea = 0
        dp = [0]*(len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j]+1 if matrix[i][j] == "1" else 0

            maxArea = max(maxArea, self.largestRectangleArea(dp))
        return maxArea