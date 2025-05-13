class Solution:
    def calculate(self, s: str) -> int:
        if '-' not in s and '+' not in s:
            return int(s.replace('(', '').replace(')', ''))
        
        def invert_sign(sign):
            return '+' if sign == '-' else '-'

        def remove_parentheses(s):
            if not('(' in s and ')' in s):
                return s
            output = ''
            stack = []
            i = 0
            while i < len(s) - 1:
                if s[i] in '+-' and s[i+1] == '(':
                    output += s[i]
                    sign = s[i]
                    stack.append(s[i+1])
                    i += 2
                    while stack and s[i] != '(':
                        if s[i] == ')':
                            stack.pop()
                            break
                        elif s[i] + s[i+1] in ('+(', '-('):
                            s = s[:i] + invert_sign(s[i]) + s[i+1:]
                            break
                        elif sign == '-' and s[i] in '+-':
                            output += invert_sign(s[i])
                        else:
                            output += s[i]
                        i += 1
                else:
                    output += s[i]
                    i += 1
            return output + s[-1]

        s = remove_parentheses(s.replace(' ', '')).replace('+-', '-').replace('-+', '+').replace('(', '').replace(')', '')
        res = 0
        s = '0' + s if not s[0].isdigit() else '0+' + s
 
        delimiters = [d for d in s if not d.isdigit()]

        for delimiter in set(delimiters):
            s = " ".join(s.split(delimiter))

        numbers = list(map(int, s.split()))

        for i in range(len(numbers)-1):
            res = numbers[i] + numbers[i+1] if delimiters[i] == '+' else numbers[i] - numbers[i+1]
            numbers[i+1] = res

        return res