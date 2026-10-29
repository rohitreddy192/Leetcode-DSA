class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        res = float("inf")

        dq = deque()

        curr_sum = 0
        
        for idx, num in enumerate(nums):
            curr_sum += num

            if curr_sum >= k:
                res = min(res, idx+1)

            while dq and curr_sum-dq[0][0]>=k:
                sum, idxL = dq.popleft()
                res = min(res, idx-idxL)
            
            while dq and dq[-1][0] >= curr_sum:
                dq.pop()
            dq.append((curr_sum, idx))
        
        return res if res!=float("inf") else -1
