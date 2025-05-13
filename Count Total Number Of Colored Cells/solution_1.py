class Solution:
    def coloredCells(self, n: int) -> int:
        # 1 - 1
        # 2 - 5     4
        # 3 - 13    8
        # 4 - 25    12

        # s = (2*a1 + d*(n-1))/2 * n
        s0 = 1
        a1 = 4
        d = 4

        if n == 1:
            return s0
        
        return s0 + (2*a1 + d*(n-2))//2 * (n-1)