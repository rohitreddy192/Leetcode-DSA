class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        leftSmaller = [0]*n
        rightSmaller = [0]*n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            leftSmaller[i] = stack[-1]+1 if stack else 0
            stack.append(i)
        
        stack.clear()
        
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            rightSmaller[i] = stack[-1]-1 if stack else n-1
            stack.append(i)
        
        maxVal = 0
        for i in range(n):
            maxVal = max(maxVal, heights[i]*(rightSmaller[i] - leftSmaller[i] + 1))
        return maxVal