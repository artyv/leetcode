class Solution:
    def jump(self, nums: List[int]) -> int:
        index_max = 0
        steps = 0
        last_index = len(nums) - 1
        for i, x in enumerate(nums):
            if x + i >= last_index:
                steps += 1
                break
            if x + i > index_max:
                steps += 1
                index_max = x + i
        return steps