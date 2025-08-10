class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = ''.join(sorted(str(n)))
        for k in range(31):
            if ''.join(sorted(str(2**k))) == s:
                return True
        return False
