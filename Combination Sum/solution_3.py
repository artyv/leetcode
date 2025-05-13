class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        for i in range(1, target+1):
            for j in itertools.combinations_with_replacement(candidates, i):
                if sum(list(j)) == target:
                    res.append(list(j))

        return res