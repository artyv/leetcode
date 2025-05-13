class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1:
            return m
        elif m == 1:
            return n
        
        a = [0] * ((m+1)*(n+1))
        a[1] = 1

        for i in range(1, m*n+1):
            if i % n != 0:
                a[i+1] += a[i]
            a[i+n] += a[i]
        return a[m*n]