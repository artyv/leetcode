class Solution:
    def minOperations(self, nums: List[int]) -> int:
        min_moves = 0
        cur_min = -1
        for n in nums:
            if n <= cur_min:
                min_moves += (cur_min + 1) - n
                cur_min += 1
            else:
                cur_min = n
        return min_moves