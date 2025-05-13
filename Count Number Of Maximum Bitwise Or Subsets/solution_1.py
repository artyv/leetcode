class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for x in nums:
            max_or |= x
        
        indices = range(len(nums))
        comb = []
        for i in range(1, len(nums)+1):
            comb += list(combinations(indices, i))
        
        counter = 0
        for x in comb:
            s_or = 0
            for i in x:
                s_or |= nums[int(i)]
            if s_or == max_or:
                counter += 1
        return counter