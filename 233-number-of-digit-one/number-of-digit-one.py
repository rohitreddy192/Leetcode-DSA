class Solution:
    def countDigitOne(self, n: int) -> int:
        cnt = 0
        i = 1
        while i<=n:
            div = i*10
            cnt += ((n//div)*i + min(max(n%div - i + 1, 0), i))
            i *= 10
        return cnt