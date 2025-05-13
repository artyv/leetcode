class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n and c_root >= 0:
            print(n, c_root)
            if n - 3**c_root >= 0:
                n -= 3**c_root
            c_root -= 1
        return n == 0