class Solution:
    def maxSum(self, nums: List[int]) -> int:
        xsum = 0
        visited = set()
        for x in nums:
            if x > 0 and x not in visited:
                xsum += x
                visited.add(x)
        if xsum == 0:
            xsum = max(nums)
        
        return xsum
