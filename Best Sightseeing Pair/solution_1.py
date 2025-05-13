class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        xmax = 0
        score_max = 0
        l = len(values)

        for i, x in enumerate(values):
            if x + i > xmax:
                for j in range(i+1, l):
                    score_max = max(score_max, (x+i)+(values[j]-j))
        return score_max