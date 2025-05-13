class Solution:
    def countAndSay(self, n: int) -> str:
        cur = '1'
        for _ in range(1, n):
            prev = cur
            cur = ''
            count = 1
            for i in range(1, len(prev)):
                if prev[i-1] == prev[i]:
                    count += 1
                else:
                    cur += str(count) + prev[i-1]
                    count = 1
            cur += str(count) + prev[-1]
        
        return cur
