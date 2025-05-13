class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def sub_sum(numbers, target, partial=[], partial_sum=0):
            if partial_sum == target:
                yield partial
            if partial_sum >= target:
                return
            for i, n in enumerate(numbers):
                remaining = numbers[i:]
                yield from sub_sum(remaining, target, partial + [n], partial_sum + n)

        return list(sub_sum(candidates, target))