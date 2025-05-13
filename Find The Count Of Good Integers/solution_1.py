from itertools import permutations

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:

        def is_palindrome(s):
            return s == s[::-1]

        good = set()
        half = (n + 1) // 2

        start = 10 ** (half - 1)
        end = 10 ** half

        for i in range(start, end):
            left = str(i)
            right = left[:-1][::-1] if n % 2 else left[::-1]
            p = left + right
            
            num = int(p)
            if num % k != 0:
                continue

            digits = list(p)
            unique_perms = set(permutations(digits))
            for perm in unique_perms:
                if perm[0] != '0':
                    good.add(''.join(perm))
        return len(good)
