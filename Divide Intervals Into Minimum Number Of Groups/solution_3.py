class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        active_intervals = 0; max_intervals = 0
        events = []
        for a, b in intervals:
            events.append((a, 1))
            events.append((b, -1))
        
        events.sort(key=lambda x: (x[0], x[1]))

        for event in events:
            active_intervals += event[1]
            max_intervals = max(max_intervals, active_intervals)
        
        return max_intervals