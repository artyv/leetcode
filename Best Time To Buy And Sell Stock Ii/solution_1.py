class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = 10**10
        profit = 0

        for p in prices:
            if p > cur_min:
                profit += p - cur_min    
            cur_min = p
        return profit