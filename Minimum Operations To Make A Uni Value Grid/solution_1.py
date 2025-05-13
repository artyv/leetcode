class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        seen_even = seen_odd = False
        nums = []

        for row in grid:
            for n in row:
                nums.append(n)
                if n % 2 == 0:
                    seen_even = True
                else:
                    seen_odd = True
        
        if seen_even and seen_odd and x % 2 == 0:
            return -1
        
        counter = 0
        nums.sort()

        len_n = len(nums)
        diff = 0
        for i in range(1, len_n):
            diff += nums[i] - nums[0]
        
        min_diff = diff if diff % x == 0 else float('inf') 

        for i in range(2, len_n):
            diff -= (nums[i-1] - nums[i-2]) * (len_n - i + 1)
            diff += (nums[i-1] - nums[i-2]) * (i - 1)
            if diff % x == 0:
                min_diff = min(min_diff, diff)
        
        return min_diff // x if min_diff != float('inf') else -1