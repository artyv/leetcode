class Solution:
    def findComplement(self, num: int) -> int:
        return 2**(int(math.log2(num)) + 1) - 1 - num