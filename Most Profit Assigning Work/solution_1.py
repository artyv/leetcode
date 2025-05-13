class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dif_prof = sorted(zip(difficulty, profit), key=lambda x: x[1], reverse=True)
        max_profit = 0
        i = 0
        for x in sorted(worker, reverse=True):
            for dif, prof in dif_prof[i:]:
                if x >= dif:
                    max_profit += prof
                    break
                i += 1
        return max_profit