MOD = 10**9 + 7
nmax = 10**5 + 1
fact = [1] * (nmax+1)
inv_fact = [1] * (nmax+1)

for i in range(1, nmax+1):
    fact[i] = fact[i - 1] * i % MOD
    inv_fact[i] = pow(fact[i], MOD - 2, MOD)

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # positions where a[i] != a[i-1]
        C_ = fact[n-1] * inv_fact[k] * inv_fact[n-k-1] % MOD

        # m for the first, m-1 for remaining
        total_ways = C_ * m * pow(m-1, n-k-1, MOD)

        return total_ways % MOD
