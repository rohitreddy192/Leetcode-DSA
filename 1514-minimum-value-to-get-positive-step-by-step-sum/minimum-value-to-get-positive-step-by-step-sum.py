class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum = 0
        for i in nums:
            sum += abs(i)
        for i in range(1,max(sum+1,100)):
            ans = i
            flag = True
            for j in nums:
                ans += j
                if ans<1:
                    flag = False
                    break
            if flag:
                return i

