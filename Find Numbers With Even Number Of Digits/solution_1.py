class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for x in nums:
            if len(str(x)) % 2 == 0:
                counter += 1
        
        return counter