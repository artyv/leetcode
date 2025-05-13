class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def prime(n):
            for x in range(2, int(sqrt(n))+1):
                if n % x == 0:
                    return False
            return True
        
        def divisors(n):
            div = set()
            for x in range(1, int(sqrt(n))+1):
                if n % x == 0:
                    div.add(x)
                    div.add(n//x)
            return div
        
        i = 1
        number = 1
        while True:
            div = [d for d in divisors(i) if prime(d) and d > 6]
            if not div:
                number = i
                n -= 1
                if n == 0:
                    break
            i += 1
        return number