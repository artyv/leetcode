class Solution:
    def calculate(self, s: str) -> int:
        def remove_parentheses(s):
            if not('(' in s and ')' in s):
                return s
            
            output = ''; stack = []; i = 0

            while i < len(s) - 1:
                if s[i]+s[i+1] == '-(':
                    output += '-'
                    stack.append('(')
                    i += 2
                    while stack and s[i] != '(':
                        if s[i] == ')':
                            stack.pop()
                            break
                        elif s[i] + s[i+1] in ('+(', '-('):
                            break
                        elif s[i] == '+':
                            output += '-'
                        elif s[i] == '-':
                            output += '+'
                        else:
                            output += s[i]
                        i += 1
                elif s[i] + s[i+1] == '+(':
                    output += '+'
                    stack.append('(')
                    i += 2
                    while stack and s[i] != '(':
                        if s[i] == ')':
                            stack.pop()
                            break
                        elif s[i] + s[i+1] in ('+(', '-('):
                            break
                        else:
                            output += s[i]
                        i += 1
                else:
                    output += s[i]
                    i += 1
            return output

        s = remove_parentheses(s.replace(' ', '')).replace('+-', '-').replace('-+', '-').replace('(', '').replace(')', '')
        res = 0
        if not s[0].isdigit():
            s = '0' + s

        while '+' in s or '-' in s:
            res += int(s[0]) + int(s[2]) if s[1] == '+' else int(s[0]) - int(s[2])
            s = '0' + s[3:]
        return res