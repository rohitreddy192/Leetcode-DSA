class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count_map = {0:1}
        cnt_odds = 0
        res = 0
        for num in nums:
            if num%2==1:
                cnt_odds += 1
            
            res += count_map.get(cnt_odds-k,0)

            count_map[cnt_odds] = count_map.get(cnt_odds, 0) + 1
            
        return res