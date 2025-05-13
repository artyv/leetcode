class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_n = (n + 1) // 2
        odd_n = n // 2
        modulo = 10**9 + 7

        return (pow(5, even_n, modulo) * pow(4, odd_n, modulo)) % modulo