from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def count_valid_permutations(digits: str) -> int:
            freq = [0] * 10
            for d in digits:
                freq[int(d)] += 1

            total = (n - freq[0]) * fac[n - 1]  # fix first digit ≠ 0
            for f in freq:
                total //= fac[f]
            return total

        fac = [factorial(i) for i in range(n + 1)]
        palindromic_digit_sets = set()

        half_len = (n + 1) // 2
        start = 10 ** (half_len - 1)
        end = 10 ** half_len

        for left in range(start, end):
            left_str = str(left)
            right_str = left_str[:-1][::-1] if n % 2 else left_str[::-1]
            palin = left_str + right_str

            if int(palin) % k == 0:
                key = ''.join(sorted(palin))
                palindromic_digit_sets.add(key)

        return sum(count_valid_permutations(s) for s in palindromic_digit_sets)
