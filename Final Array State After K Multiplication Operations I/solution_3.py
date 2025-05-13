class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums_copy = nums[:]
        heapq.heapify(nums_copy)
        l = len(nums)
        for _ in range(k):
            temp = heapq.heappop(nums_copy)
            for i in range(l):
                if nums[i] == temp:
                    nums[i] = temp * multiplier
                    break
            heapq.heappush(nums_copy, temp * multiplier)
        
        return nums