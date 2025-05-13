class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [n for row in grid for n in row]
        nums.sort()

        base = nums[0]
        for num in nums:
            if (num - base) % x != 0:
                return -1

        # median is the element we need, don't care if the number of elements is odd or even
        median = nums[len(nums) // 2]

        diff = 0
        for num in nums:
            diff += abs(num - median)
        
        return diff // x