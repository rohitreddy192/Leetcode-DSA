class Solution:
    def maxEnvelopes(self, arr: List[List[int]]) -> int:
        arr.sort(key=lambda x: (x[0], -x[1])) #
        #  - x[1] because [[4,5],[4,6],[6,7],[2,3],[1,1]] this test case 
        # LEts say 4,5 and 4,6 can't be considered at the same time as width is same only one should be considered so to eliminate that we sort x[1] heights in descending order.
        print(arr)

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx==len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            
            return len(dp)
        
        return lis([i[1] for i in arr])




        # envelopes.sort()
        
        # dp = {}
        # def solve(i,prev):
        #     if i==len(envelopes):
        #         return 0

        #     if (i,prev) in dp: return dp[(i,prev)]

        #     not_pick = 0 + solve(i+1,prev)
        #     pick = 0
        #     if prev==-1 or (envelopes[prev][0]<envelopes[i][0] and envelopes[prev][1]<envelopes[i][1]):
        #         pick = 1 + solve(i+1, i)
            
        #     dp[(i,prev)] = max(pick,not_pick)
        #     return dp[(i,prev)]
        