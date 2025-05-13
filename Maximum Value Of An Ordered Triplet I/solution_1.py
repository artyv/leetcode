class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        x_max = 0
        n = len(nums)

        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    x_max = max(x_max, (nums[i] - nums[j]) * nums[k])
        return x_max