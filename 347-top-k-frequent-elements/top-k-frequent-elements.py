class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        hp = []
        for u,v in d.items():
            heapq.heappush(hp, (-1*v,u))
        
        ans = []
        for _ in range(k):
            if not hp:
                return ans
            
            _, val = heapq.heappop(hp)
            ans.append(val)

        return ans