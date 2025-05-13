class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        counter = Counter(num)
        n = len(num)
        MODULO = 10**9 + 7
        
        @lru_cache(None)
        def backtrack(pos, even_sum, odd_sum, counts):
            if pos == n:
                return int(even_sum == odd_sum)

            total = 0
            is_even = pos % 2 == 0
            for d in range(10):
                c = counts[d]
                if c == 0:
                    continue
                new_counts = list(counts)
                new_counts[d] -= 1
                digit = d
                if is_even:
                    total += backtrack(pos + 1, even_sum + digit, odd_sum, tuple(new_counts))
                else:
                    total += backtrack(pos + 1, even_sum, odd_sum + digit, tuple(new_counts))
                total %= MODULO
            return total

        # Convert counts to a tuple indexed by digit 0–9
        initial_counts = [counter[str(i)] for i in range(10)]
        return backtrack(0, 0, 0, tuple(initial_counts))