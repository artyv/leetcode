class Solution:
    def findComplement(self, num: int) -> int:
        return 2**(len(format(num, '0b'))) - 1 - num