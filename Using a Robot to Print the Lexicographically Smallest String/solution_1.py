class Solution:
    def robotWithString(self, s: str) -> str:
        len_s = len(s)
        aux = [''] * len_s # min letter onwards 
        min_let = 'z'
        for i in range(len_s-1, -1, -1):
            if s[i] < min_let:
                min_let = s[i]
            aux[i] = min_let
        
        stack = []
        res = ''
        i = 0
        while i < len_s or stack:
            while i < len_s and (not stack or stack[-1] > aux[i]):
                stack.append(s[i])
                i += 1
            res += stack.pop()
        
        return res
