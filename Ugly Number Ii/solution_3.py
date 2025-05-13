class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def generate_prime(n):
            x = 7
            prime_divisors = []
            while n:
                for d in range(2, int(sqrt(x))+1):
                    if x % d == 0:
                        break
                else:
                    prime_divisors.append(x)
                    n -= 1
                x += 1
            return prime_divisors
        
        
        primes = generate_prime(4000)
        print(primes)
        i = 1
        number = 1
        while True:
            if any(i % x == 0 for x in primes):
                i += 1
                continue
            else:
                number = i
                n -= 1
                if n == 0:
                    break
            i += 1
        return number