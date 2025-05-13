class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = list(s.split())
        if len(pattern) != len(s_list):
            return False
        
        d = {}
        for i, c in enumerate(pattern):
            if d.get(c, 0) == 0:
                if s_list[i] in d.values():
                    return False
                d[c] = s_list[i]
            else:
                if d[c] != s_list[i]:
                    return False
        return True