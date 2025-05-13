class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        smax = 0
        sc = nums[0]
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                sc += nums[i+1]
            else:
                smax = max(smax, sc)
                sc = nums[i+1]
        smax = max(smax, sc)
        return smax