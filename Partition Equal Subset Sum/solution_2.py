class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        
        target = s // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for x in nums:
            for y in range(target, x-1, -1):
                if dp[y-x]:
                    dp[y] = True
        
        return dp[target]