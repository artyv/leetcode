class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        a = set()
        min_moves = 0
        for n in nums:
            while n in a:
                n += 1
                min_moves += 1
            a.add(n)
        return min_moves