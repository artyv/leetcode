class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count_1 = nums.count(1)
        aux = nums * 2
        min_swaps = 10**10

        for i in range(len(nums)):
            min_swaps = min(min_swaps, aux[i:i+count_1].count(0))
        
        return min_swaps
