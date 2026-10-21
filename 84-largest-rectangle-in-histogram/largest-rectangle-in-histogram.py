class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        n = len(nums)
        def nextSmallerElementCompFunc(nums):
            nse = nums[:]
            st = []
            for i in range(n-1,-1,-1):
                while st and nums[st[-1]]>=nums[i]:
                    st.pop()
                nse[i] = n if not st else st[-1]
                st.append(i)
            
            return nse

        def prevSmallerElementCompFunc(nums):
            nse = nums[:]
            st = []
            for i in range(n):
                while st and nums[st[-1]]>=nums[i]:
                    st.pop()
                nse[i] = -1 if not st else st[-1]
                st.append(i)
            
            return nse


        nextSmallerElementArr= nextSmallerElementCompFunc(nums)
        prevSmallerElementArr = prevSmallerElementCompFunc(nums)

        maxArea = 0
        for idx in range(n):
            width = nextSmallerElementArr[idx]-prevSmallerElementArr[idx]-1
            maxArea = max(maxArea, (width*nums[idx]))
        
        return maxArea