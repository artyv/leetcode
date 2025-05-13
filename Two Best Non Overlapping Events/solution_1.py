class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        queue = []
        events.sort(key=lambda x: x[0])
        max_val = 0; max_sum = 0

        for event in events:
            while queue and queue[0][0] < event[0]:
                max_val = max(max_val, queue[0][1])
                heapq.heappop(queue)

            max_sum = max(max_sum, max_val + event[2])
            heapq.heappush(queue, (event[1], event[2]))

        return max_sum