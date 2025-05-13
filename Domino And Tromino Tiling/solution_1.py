class Solution:
    def numTilings(self, n: int) -> int:
        # n = 1; res = 1
        # n = 2; res = 2
        # n = 3; res = 5
        # n = 4; res = 11

        if n <= 2:
            return n
        elif n == 3:
            return 5

        MODULO = 10**9 + 7
        dp = [0] * (n+1)
        dp[1] = 1; dp[2] = 2; dp[3] = 5

        for i in range(4, n+1):
            dp[i] = 2*dp[i-1] + dp[i-3]
        
        return dp[n] % MODULO