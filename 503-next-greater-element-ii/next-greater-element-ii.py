class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        n = len(nums)
        nge = nums[:]
        for i in range(2*n-1,-1,-1):
            while st and nums[i%n]>=st[-1]:
                st.pop()
            if(i<n):
                nge[i] = st[-1] if st else -1
            st.append(nums[i%n])
        
        return nge