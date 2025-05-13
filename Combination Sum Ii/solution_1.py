class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if sum(candidates) < target:
            return res
        elif sum(candidates) == target:
            res.append(candidates)
            return res
        
        aux = sorted([x for x in candidates if x <= target])
        l = len(aux)

        def backtrack(start_index, comb, target):
            if target == 0:
                res.append(comb)
                return
            for i in range(start_index, l):
                if i > start_index and aux[i-1] == aux[i]:
                    continue
                if aux[i] > target:
                    break
                backtrack(i+1, comb + [aux[i]], target - aux[i])

        backtrack(0, [], target)
        return res
