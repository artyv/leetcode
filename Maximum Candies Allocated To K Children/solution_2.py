class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 0; r = max(candies)
        max_candies = 0

        while l < r:
            mid = (l+r+1) // 2

            num_piles = 0
            for p in candies:
                num_piles += p // mid
            if num_piles >= k:
                max_candies = mid
                l = mid
            else:
                r = mid-1

        return max_candies