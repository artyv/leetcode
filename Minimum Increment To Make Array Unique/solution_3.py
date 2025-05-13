class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        a = set()
        nums.sort()
        min_moves = 0
        cur_min = 1
        for n in nums:
            if n in a:
                min_moves += (cur_min + 1) - n
                cur_min += 1
                a.add(cur_min)
            else:
                cur_min = n
                a.add(n)
        return min_moves