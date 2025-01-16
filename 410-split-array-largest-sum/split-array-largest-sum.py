class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isPossible(mid):
            cnt = 1
            currentCnt = 0
            for num in nums:
                if currentCnt + num > mid:
                    currentCnt = num
                    cnt += 1
                    if cnt > k:
                        return False
                else:
                    currentCnt += num
            return True


        low = max(nums)
        high = sum(nums)
        ans = 0
        while low<=high:
            mid = (low+high)//2
            if isPossible(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans