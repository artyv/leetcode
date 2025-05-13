class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        index_max = 0
        steps = 0
        last_index = len(nums) - 1
        for i, x in enumerate(nums):
            if x + i >= last_index:
                return steps + 1
            if x + i > index_max:
                steps += 1
                index_max = x + i
        return steps