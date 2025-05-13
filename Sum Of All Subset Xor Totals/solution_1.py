class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = [[]]

        for elem in nums:
            new_subsets = [subset + [elem] for subset in subsets]
            subsets.extend(new_subsets)

        xor_sum = 0
        for lst in subsets:
            temp = 0
            for x in lst:
                temp ^= x
            xor_sum += temp

        return xor_sum
