class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        st = []
        leftsmall = [0] * n
        rightsmall = [0] * n
        
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            
            leftsmall[i] = st[-1] + 1 if st else 0
            st.append(i)
        
        st.clear()
        
        for i in range(n - 1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            
            rightsmall[i] = st[-1] - 1 if st else n - 1
            st.append(i)
        
        max_area = 0
        for i in range(n):
            max_area = max(max_area, heights[i] * (rightsmall[i] - leftsmall[i] + 1))
        
        return max_area