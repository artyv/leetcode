class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        left, right = meetings[0]
        counter = 0

        for a,b in meetings:
            if a > right + 1:
                counter += right - left + 1
                left = a
            right = max(right, b)

        counter += right - left + 1       

        return days - counter