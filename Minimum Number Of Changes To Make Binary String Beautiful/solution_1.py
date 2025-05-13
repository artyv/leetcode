class Solution:
    def minChanges(self, s: str) -> int:
        s_shortened = ''
        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                s_shortened += s[i] + s[i+1]
        
        return len(s_shortened) // 2