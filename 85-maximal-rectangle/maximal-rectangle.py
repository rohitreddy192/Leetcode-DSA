class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        maxArea = 0
        dp = [0]*(len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j]+1 if matrix[i][j] == "1" else 0

            maxArea = max(maxArea, self.largestRectangleArea(dp))
        return maxArea