class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal

        counter = 0
        while xor:
            counter += (xor & 1)
            xor >>= 1
        return counter
        
