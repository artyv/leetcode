class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []

        def createSubsets(lst):
            if not lst:
                return [[]]
            
            first = lst[0]
            rest = lst[1:]

            rest_subsets = createSubsets(rest)

            with_first = [[first] + s for s in rest_subsets]

            return rest_subsets + with_first
        
        subsets = createSubsets(nums)

        xor_sum = 0
        for lst in subsets:
            temp = 0
            for x in lst:
                temp ^= x
            xor_sum += temp

        return xor_sum
