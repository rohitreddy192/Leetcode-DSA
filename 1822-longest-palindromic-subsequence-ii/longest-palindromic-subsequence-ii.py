class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1 = s
        text2 = s[::-1]

        n = len(s)

        dp = [[[0 for _ in range(26)]
               for i in range(n + 1)]
              for j in range(n + 1)]

        maxi = 0

        for i in range(1, n + 1):

            for j in range(1, n + 1):

                # Don't take current character
                for c in range(26):
                    dp[i][j][c] = max(
                        dp[i-1][j][c],
                        dp[i][j-1][c]
                    )

                # Characters match
                if text1[i-1] == text2[j-1]:

                    current = ord(text1[i-1]) - ord('a')

                    # We need to make sure we are using
                    # two different positions in s
                    if i + j <= n:

                        # First pair
                        dp[i][j][current] = max(
                            dp[i][j][current],
                            2
                        )

                        # Add current pair around an
                        # existing palindrome
                        for previous in range(26):

                            if previous != current:

                                dp[i][j][current] = max(
                                    dp[i][j][current],
                                    dp[i-1][j-1][previous] + 2
                                )

                maxi = max(
                    maxi,
                    max(dp[i][j])
                )

        return maxi