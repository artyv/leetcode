class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = len(prices)
        answer = [0] * l
        answer[-1] = prices[-1]
        for i in range(l-1):
            for j in range(i+1, l):
                if prices[j] <= prices[i]:
                    answer[i] = prices[i] - prices[j]
                    break
            else:
                answer[i] = prices[i]
        return answer