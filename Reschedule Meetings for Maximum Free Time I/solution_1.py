class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = [startTime[0]]
        n = len(startTime)
        for i in range(n-1):
            gaps.append(startTime[i+1]-endTime[i])

        gaps.append(eventTime-endTime[-1])
        
        max_gap = cur_sum = sum(gaps[:k+1])
        l, r = 1, k+1
        while r < len(gaps):
            cur_sum += gaps[r] - gaps[l-1]
            max_gap = max(max_gap, cur_sum)
            l += 1
            r += 1

        return max_gap
