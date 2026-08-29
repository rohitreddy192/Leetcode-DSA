class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnd, vt = 0, 0
        for i in nums:
            if (vt == 0):
                cnd = i
            if(cnd==i):
                vt += 1
            else:
                vt -= 1
        return cnd