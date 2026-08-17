class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        d = dict()

        for task in tasks:
            d[task] = d.get(task,0) + 1

        ans = 0

        for i,j in d.items():
            if j==1: return -1
            elif j%3==0:
                ans += j//3
            else:
                ans += j//3 + 1
                
        return ans