class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        maxCnt = 0
        for i in nums:
            num = i
            if num-1 not in hs:
                cnt = 1
                while num+1 in hs:
                    cnt += 1
                    num += 1
                maxCnt = max(maxCnt,cnt)
        return maxCnt