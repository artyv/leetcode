class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        arrows = 0
        max_right = points[0][1]
        for start, end in points:
            if max_right >= start:
                max_right = min(max_right, end)
            else:
                arrows += 1
                max_right = end
        arrows += 1
        return arrows