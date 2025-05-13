class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])

        p = product('01', repeat=n)
        p_set = set()
        for x in p:
            p_set.add(''.join(x))

        for s in nums:
            if s in p_set:
                p_set.remove(s)
        
        return next(iter(p_set))
