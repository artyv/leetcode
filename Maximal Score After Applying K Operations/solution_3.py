class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = []
        score = 0
        for x in nums:
            heapq.heappush(max_heap, -x) # heappop() returns the smallest, we need the largest number, so trick with '-'
        
        for _ in range(k):
            temp = -heapq.heappop(max_heap)
            score += temp
            heapq.heappush(max_heap, -ceil(temp/3)) # this way, because ceil(temp/3) for negative will behave differently

        return score