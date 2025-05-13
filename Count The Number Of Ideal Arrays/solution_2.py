class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        def prime_factors(x):
            i = 2
            res = Counter()
            while i * i <= x:
                while x % i == 0:
                    res[i] += 1
                    x //= i
                i += 1
            if x > 1:
                res[x] += 1
            return res
        
        MOD = 10**9 + 7
        MAX = 10
        
        fact = [1] * MAX
        for i in range(1, MAX):
            fact[i] = (fact[i-1] * i) % MOD
        
        inv_fact = [1] * MAX
        inv_fact[-1] = pow(fact[-1], MOD-2, MOD)
        for i in reversed(range(1, MAX)):
            inv_fact[i-1] = (inv_fact[i] * i) % MOD
        
        def combs(n, k):
            if n < k or k < 0:
                return 0
            return (fact[n] * inv_fact[k]) % MOD * (inv_fact[n-k] % MOD)
        
        counter = 0
        for x in range(1, maxValue+1):
            primes = prime_factors(x)
            temp = 1
            for power in primes.values():
                temp = (temp * combs(power + n - 1, power)) % MOD
            counter = (counter + temp) % MOD
        
        return counter