from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nmin = min(nums)
        nmax = max(nums)
        count = [0] * (nmax - nmin + 1)

        for n in nums:
            count[n - nmin] += 1
        
        remain = k

        for i in range(nmax - nmin, -1, -1):
            remain -= count[i]
            if remain <= 0:
                return i + nmin