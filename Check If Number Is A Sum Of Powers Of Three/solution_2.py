class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        c_root = int(n**(1/3))
        while n and c_root >= 0:
            if n - 3**c_root >= 0:
                n -= 3**c_root
            c_root -= 1
        return n == 0