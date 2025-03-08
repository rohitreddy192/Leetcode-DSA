class Solution:
    def longestPalindrome(self, s: str) -> int:
        mpp = sorted(Counter(s).values(), reverse = True)
        max_1_odd = False
        cnt = 0
        for i in mpp:
            if i%2==0:
                cnt += i
            else:
                max_1_odd = True
                cnt += (i-1)
        if max_1_odd:
            cnt += 1
        return cnt