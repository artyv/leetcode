class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [0] * (n+1)

        @lru_cache
        def helper(n):
            if nums[n]:
                return nums[n]
            if n == 1 or n == 2:
                return n
            nums[n] = helper(n-1) + helper(n-2)
            return nums[n]
        
        return helper(n)