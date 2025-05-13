class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        l = len(values)
        max_score = 0
        for i in range(l-1):
            for j in range(i+1, l):
                max_score = max(max_score, values[i]+values[j]+i-j)
        return max_score