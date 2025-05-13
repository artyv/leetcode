class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        a = []
        for i in range(n+1):
            a.append(format(i, '0b').count('1'))
        return a