class Solution:
    def clearDigits(self, s: str) -> str:
        ans = []

        for c in s:
            if c.isdigit() and ans:
                ans.pop()
            else:
                ans.append(c)
        
        return ''.join(ans)