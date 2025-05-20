class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        if len(queries) < max(nums):
            return False

        len_nums = len(nums)
        diff_sum = [0] * len_nums
        for l, r in queries:
            diff_sum[l] -= 1
            if r < len_nums - 1:
                diff_sum[r+1] += 1
            
        nums[0] += diff_sum[0]
        for i in range(1, len_nums):
            diff_sum[i] += diff_sum[i-1]
            nums[i] += diff_sum[i]
        
        return all(x <= 0 for x in nums)
