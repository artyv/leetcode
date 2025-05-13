class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        aux = [float('inf')]*l
        aux[-1] = prices[-1]
        for i in range(l-2, -1, -1):
            aux[i] = max(aux[i+1], prices[i])
        
        profit = 0
        for i in range(l-1):
            profit = max(profit, aux[i] - prices[i])
        
        return profit