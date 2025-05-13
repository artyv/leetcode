class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        if len(nums) >= 8:
            aux = nums[:4] + nums[-4:]
        else:
            aux = nums
        min_diff = 10**10
        step = len(aux) - 4

        for i in range(len(aux) - step):
            min_diff = min(min_diff, aux[i+step] - aux[i])

        return min_diff