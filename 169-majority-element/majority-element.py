class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnd, vt = -1, 0
        for num in nums:
            if cnd!=num:
                if vt==0:
                    cnd=num
                    vt=1
                else:
                    vt -= 1
            else:
                vt += 1
        
        return cnd