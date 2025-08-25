import math

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        evens = 5   # choices for even indices
        primes = 4  # choices for odd indices

        evenPower = (n + 1) // 2  # ceil(n/2)
        oddPower = n // 2         # floor(n/2)

        return (pow(evens, evenPower, MOD) * pow(primes, oddPower, MOD)) % MOD
