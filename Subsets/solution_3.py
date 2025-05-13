from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[], nums]
        l = 1

        while l < len(nums):
            for x in combinations(nums, l):
                res.append(list(x))
            l += 1
        return res 