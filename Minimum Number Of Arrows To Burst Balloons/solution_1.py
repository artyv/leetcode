class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        arrows = 0
        max_right = points[0][1]
        for i in range(len(points)-1):
            if max_right < points[i+1][0]:
                arrows += 1
                max_right = points[i+1][1]
            else:
                max_right = min(max_right, points[i+1][1])
        arrows += 1
        return arrows