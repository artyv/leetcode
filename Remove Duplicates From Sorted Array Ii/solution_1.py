class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}; k = 0

        for i, x in enumerate(nums):
            if d.get(x, 0) < 2:    
                d[x] = d.get(x, 0) + 1
                nums[k] = x
                k += 1
        return k