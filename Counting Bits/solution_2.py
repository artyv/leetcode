class Solution:
    def countBits(self, n: int) -> List[int]:
        a = [0] * (n+1)
        for i in range(1, n+1):
            if i % 2 == 1:
                a[i] = a[i-1] + 1
            else:
                a[i] = a[i//2]
        return a