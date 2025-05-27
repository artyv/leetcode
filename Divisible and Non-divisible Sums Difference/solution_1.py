class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # arithmetic progression is smarter
        cnt = n // m   # count non-divisible
        num2 = m * (1 + cnt) * cnt // 2
        total_sum = (n + 1) * n // 2
        return total_sum - 2*num2
