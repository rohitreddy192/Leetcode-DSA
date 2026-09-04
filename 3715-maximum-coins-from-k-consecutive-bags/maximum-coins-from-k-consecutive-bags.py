class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def slide(coins):
            coins.sort()

            res = curr = j = 0

            for i in range(len(coins)):
                curr += (coins[i][1]-coins[i][0]+1)*coins[i][2]
                while coins[j][1] < coins[i][1]-k+1:
                    curr -= (coins[j][1]-coins[j][0]+1)*coins[j][2]
                    j += 1
                
                part = max(0, coins[i][1] - k - coins[j][0] + 1) * coins[j][2]
                res = max(res, curr-part)
            return res
        
        return max(slide(coins),slide([[-r,-l,w] for l,r,w in coins]))