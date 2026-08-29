class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnd1, cnd2,c1,c2 = 0,0,0,0
        for i in nums:
            if i==cnd1: c1+=1
            elif i==cnd2: c2+=1
            elif c1==0: 
                cnd1 = i
                c1 = 1
            elif c2 == 0:
                cnd2 = i
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        c1, c2, n, l = 0, 0, len(nums), []
        for i in nums:
            if cnd1==i: c1+=1
            elif cnd2 == i: c2 += 1
        if c1>n/3: l.append(cnd1)
        if c2>n/3: l.append(cnd2)

        return l