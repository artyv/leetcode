from itertools import product
from math import ceil

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        for r in range(ceil(target/max(candidates)), target//min(candidates) + 1):
            p = product(candidates, repeat=r)
            for x in p:
                x.sort()
                if sum(x) == target and x not in res:
                    res.append(list(x))
        return res