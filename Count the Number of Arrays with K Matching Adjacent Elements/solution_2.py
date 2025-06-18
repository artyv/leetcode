class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        fact = [1] * (n+1)
        inv_fact = [1] * (n+1)

        for i in range(1, n+1):
            fact[i] = fact[i - 1] * i % MOD
        
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
        # positions where a[i] != a[i-1]
        C_ = fact[n-1] * inv_fact[k] % MOD * inv_fact[n-k-1] % MOD

        # m for the first, m-1 for remaining
        total_ways = C_ * m % MOD * pow(m-1, n-k-1, MOD)

        return total_ways % MOD
