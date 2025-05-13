class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []
        for passes, total in classes:
            gain = (passes+1) / (total+1) - passes/total
            heapq.heappush(max_heap, (-gain, passes, total))

        for _ in range(extraStudents):
            current_gain, passes, total = heapq.heappop(max_heap)
            heapq.heappush(max_heap,
                (
                    (-1)* ((passes+2) / (total+2) - (passes+1)/(total+1)),
                    passes + 1,
                    total + 1,
                ),
            )

        pass_ratio = 0
        while max_heap:
            _, passes, total = heapq.heappop(max_heap)
            pass_ratio += passes / total
        return pass_ratio / len(classes)