class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        groups = 0
        intervals.sort(key=lambda x: x[0])
        indices = []
        while intervals:
            x, y = 0, 0
            for i in range(len(intervals)):
                if intervals[i][0] > y:
                    x, y = intervals[i]
                    indices.append(i)
            while indices:
                intervals.pop(indices.pop())
            groups += 1
        
        return groups