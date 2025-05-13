class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = 10**10
        smax = 0 

        for p in prices:
            if p < cur_min:
                cur_min = p
            smax = max(smax, p - cur_min)
        return smax