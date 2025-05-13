class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = format(start ^ goal, '0b')

        return sum(list(map(int, xor)))
        
