from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a = [-10000]

        for x in nums:
            if x > a[0]:
                heappush(a, x)
                if len(a) > k:
                    heappop(a)
        return a[0]