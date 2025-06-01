class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total_ways = 0
        for i in range(min(limit, n) + 1):
            low_j = max(0, n - i - limit)
            high_j = min(limit, n - i)
            if low_j <= high_j:
                total_ways += (high_j - low_j + 1)
        return total_ways
