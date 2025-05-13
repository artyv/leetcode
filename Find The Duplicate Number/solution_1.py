class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if d.get(n) == None:
                d[n] = '1'
            else:    
                return n
            