class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Instead of O(n*logn) sorting, can use Boyer-Moore Majority Vote Algorithm
        dominant, count = None, 0

        for x in nums:
            if count == 0:
                dominant, count = x, 1
            elif x == dominant:
                count += 1
            else:
                count -= 1
        
        # One more optimization: loop through once by having left and right counters
        left_count = 0
        right_count = nums.count(dominant)
        n = len(nums)

        for i in range(n-1):
            if nums[i] == dominant:
                left_count += 1
                right_count -= 1
            
            if left_count * 2 > (i + 1) and right_count * 2 > (n - i - 1):
                return i
        
        return -1
