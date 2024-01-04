class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i]  = d.get(i,0) + 1
        print(d)
        cnt = 0
        for i,j in d.items():
            if j == 1:
                return -1
            elif j%3==0:
                cnt += ((j)//3)
            elif j%2==0:
                cnt += 1
                j = j-2
                if j%3==0:
                    cnt += ((j)//3)
                    j = 0
                    continue
                while j%2 == 0:
                    cnt += 1
                    j = j-2
                    if j%3 == 0:
                        cnt += ((j)//3)
                        j = 0
                        break
            else:
                j = j-3
                cnt += 1
                while j%2 == 0:
                    cnt += 1
                    j = j-2
                    if j%3 == 0:
                        cnt += ((j)//3)
                        j = 0
                        break
        return cnt            
                