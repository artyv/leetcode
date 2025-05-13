class Solution:
    def reverseParentheses(self, s: str) -> str:
        opened = []
        output = ''

        for i in range(len(s)):
            if s[i] == '(':
                opened.append(i)
            elif s[i] == ')':
                index = opened.pop()
                output = output[:index] + output[index:i+1][::-1]
            output += s[i]
        return output.replace('(', '').replace(')', '')
            
            
        