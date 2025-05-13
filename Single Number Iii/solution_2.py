class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a = set()
        for x in nums:
            if x in a:
                a.remove(x)
            else:
                a.add(x)
        return a