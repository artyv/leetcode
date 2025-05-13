class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dif_prof = sorted([(difficulty[i], profit[i]) for i in range(len(profit))], reverse=True)
        max_profit = 0
        for x in worker:
            for dif, prof in dif_prof:
                if x >= dif:
                    max_profit += prof
                    break
        return max_profit