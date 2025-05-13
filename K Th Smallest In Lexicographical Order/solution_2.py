class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        res = []
        cur = 1

        for _ in range(n):
            res.append(cur)
            if len(res) == k:
                return res[-1]

            if cur * 10 <= n:
                cur *= 10
            else:
                while cur % 10 == 9 or cur >= n:
                    cur //= 10 
                cur += 1

        return res[-1]