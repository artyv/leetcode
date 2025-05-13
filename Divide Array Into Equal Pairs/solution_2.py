class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = dict()

        for x in nums:
            d[x] = d.get(x, 0) + 1
        
        return all(x % 2 == 0 for x in d.values())