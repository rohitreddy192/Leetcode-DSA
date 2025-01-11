class Solution:
    def numDecodings(self,s):
        n = len(s)
        def solve(i,dp):
            if i==n: return 1
            if i>n or s[i]=="0": return 0

            if i in dp: return dp[i]

            pick_1 = solve(i+1,dp)
            pick_2 = 0
            if 10<=int(s[i:i+2])<=26 and i+1 < n:
                pick_2 = solve(i+2,dp)

            dp[i] = pick_1 + pick_2
            return dp[i]
        
        dp = {}
        return solve(0,dp)



        # if not s or len(s) == 0:
        #     return 0
        
        # n = len(s)
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1 if s[0] != '0' else 0
        
        # for i in range(2, n + 1):
        #     first = int(s[i - 1:i])  # Current character as an integer
        #     second = int(s[i - 2:i])  # Last two characters as an integer
            
        #     if 1 <= first <= 9:
        #         dp[i] += dp[i - 1]
        #     if 10 <= second <= 26:
        #         dp[i] += dp[i - 2]
        
        # return dp[n]
