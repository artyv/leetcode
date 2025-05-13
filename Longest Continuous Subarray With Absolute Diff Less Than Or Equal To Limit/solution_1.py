class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = deque()
        min_queue = deque()  

        l = 0

        for n in nums:
            # max_queue and min_queue in decreasing order
            while max_queue and n > max_queue[-1]:
                max_queue.pop()
            max_queue.append(n)

            while min_queue and n < min_queue[-1]:
                min_queue.pop()
            min_queue.append(n)

            if max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[l]:
                    max_queue.popleft()
                if min_queue[0] == nums[l]:
                    min_queue.popleft()
                l += 1
        return len(nums) - l