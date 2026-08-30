class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxLen = 0
        for n in s:
            if(n-1) not in s:
                length = 0
                while (n+length) in s:
                    length += 1
                maxLen = max(maxLen,length)
        return maxLen