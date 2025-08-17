class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def fac(num):
            factorial = 1
            for i in range(1, num+1):
                factorial *= i
            return factorial 

        # Number of ways you can arrange c cols and r rows = (r+c)!/r!c!
        r = m - 1
        d = n - 1
        return fac(r+d)//(fac(r)*fac(d))    