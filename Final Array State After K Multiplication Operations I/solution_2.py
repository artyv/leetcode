class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(x, i) for i,x in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            val, i = heapq.heappop(heap)
            nums[i] = val * multiplier
            heapq.heappush(heap, (nums[i], i))
        
        return nums