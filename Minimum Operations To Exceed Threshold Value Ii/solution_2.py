class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        number_operations = 0
        while k > heapq.nsmallest(1, nums)[0] and len(nums) >= 2:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, min(x, y)*2 + max(x, y))
            number_operations += 1
        return number_operations