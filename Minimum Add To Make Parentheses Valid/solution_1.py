class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        counter = 0
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    counter += 1
                
        return counter + len(stack)