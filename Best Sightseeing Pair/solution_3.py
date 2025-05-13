class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        xmax = 0
        score_max = 0

        for i, x in enumerate(values):
            if xmax + x - i > score_max:
                score_max = xmax + x - i
            if x + i > xmax:
                xmax = x + i


        return score_max