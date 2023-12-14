class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        maxCnt = 0
        for i in nums:
            num = i
            cnt = 0
            while num-1 in hs:
                num -= 1
            while num in hs:
                maxCnt = max(maxCnt,cnt + 1)
                hs.remove(num)
                num = num + 1     
                cnt += 1
        return maxCnt