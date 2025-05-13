class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        result = ''
        for i in range(len(s)):
            if i == 0:
                if s[i] == '-':
                    result += '-'
                    continue
            if not s[i].isdigit():
                break
            result += s[i]
        
        if not result or not(len(result) == 1 and result == '-'):
            result = int(result)
        else:
            return 0
        if result < -2**31:
            result = -2**31
        elif result > 2**31 - 1:
            result = 2**31 - 1
        
        return result
            