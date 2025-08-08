class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1
        
        m = ceil(n/25) # would use 25ml as a portion

        @lru_cache(None)
        def f(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return 0.25 * (
                f(a - 4, b) +
                f(a - 3, b - 1) +
                f(a - 2, b - 2) +
                f(a - 1, b - 3)
            )

        return f(m, m)
