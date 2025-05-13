class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        result = ''
        for i in range(len(s)):
            if i == 0:
                if s[i] in '+-':
                    result += s[i]
                    continue
            if not s[i].isdigit():
                break
            result += s[i]
        
        if not result or (len(result) == 1 and (result == '-' or result == '+')):
            return 0
        else:
            result = int(result)
        if result < -2**31:
            result = -2**31
        elif result > 2**31 - 1:
            result = 2**31 - 1
        
        return result
            