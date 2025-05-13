class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        aux = [0] * n
        points_max = 0

        for i, (p, b) in enumerate(questions):
            points = p
            j = i + (b + 1)
            while j < n:
                points += questions[j][0]
                j += questions[j][1] + 1
            points_max = max(points_max, points)
        
        return points_max