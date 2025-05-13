from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, l, cur, res):
            if l == len(nums):
                res.append(cur)
                return

            dfs(nums, l + 1, cur + [nums[l]], res)
            dfs(nums, l + 1, cur, res)
        
        dfs(nums, 0, [], res)
        return res