class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        accum = set()
        accum.add(nums[0]%k)
        for x in nums[1:]:

            accum = set([(acc+x)%k for acc in accum])

            if 0 in accum:
                return True
            accum.add(x % k)
        return False
