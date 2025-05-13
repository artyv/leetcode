class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = len(prices)
        answer = prices.copy()
        stack = deque()

        for i in range(l):
            while stack and prices[stack[-1]] >= prices[i]:
                answer[stack.pop()] -= prices[i]
            stack.append(i)
        return answer