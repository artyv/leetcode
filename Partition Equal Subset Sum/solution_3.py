class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        left_sum, right_sum = nums[0], nums[-1]

        for i in range(1, len(nums)-1):
            if left_sum <= right_sum:
                left_sum += nums[i]
            else:
                right_sum += nums[i]
        
        return left_sum == right_sum