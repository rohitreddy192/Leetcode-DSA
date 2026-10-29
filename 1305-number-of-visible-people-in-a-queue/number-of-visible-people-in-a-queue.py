class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        stack = []
        res = [0] * n

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
                res[i] += 1

            if stack:
                res[i] += 1

            stack.append(i)

        return res