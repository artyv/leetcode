class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        merged_intervals = []
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]

        for x in intervals:
            if prev_end >= x[0]:
                prev_end = max(x[1], prev_end)
            else:
                merged_intervals.append([prev_start, prev_end])
                prev_start, prev_end = x[0], x[1]

        merged_intervals.append([prev_start, prev_end])

        return merged_intervals