class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if s < target:
            return 0
        elif s == target:
            return 1 + nums.count(0)
        
        d = defaultdict(int)
        d[0] = 1

        for num in nums:
            dp = defaultdict(int)
            for k, v in d.items():
                dp[k + num] += v
                dp[k - num] += v
            d = dp

        return d[target]