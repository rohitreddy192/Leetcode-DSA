class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def ul():
            l, h = 0, len(nums)
            a = h
            while l<h:
                m = (l+h)//2
                if nums[m]>target:
                    h = m
                else:
                    l = m+1
            
            return l

        def ll():
            l, h = 0, len(nums)
            a = h
            while l<h:
                m = (l+h)//2
                if nums[m]>=target:
                    h = m
                else:
                    l = m+1
            
            return l

        return (ul()-ll())*2 > len(nums) 