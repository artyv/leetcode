class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 0; r = max(candies)

        while l < r:
            mid = (l+r+1) // 2

            num_piles = sum(p // mid for p in candies)
 
            if num_piles >= k:
                l = mid
            else:
                r = mid-1

        return r