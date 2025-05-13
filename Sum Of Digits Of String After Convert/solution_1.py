class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ''
        reference_value = 96
        for c in s:
            res += str(ord(c)-reference_value)
        
        for _ in range(k):
            res = str(sum(list(map(int, res))))
        return int(res)