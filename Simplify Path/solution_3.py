class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [path[0]]
        while '//' in path:
            path = path.replace('//', '/')

        parts = [p for p in path.split('/') if p != '']
        for c in parts:
            if c == '..':
                if len(stack) > 1:
                    stack.pop()
                    stack.pop()
            elif c != '.':
                stack.append(c)
                stack.append('/')
        
        if len(stack) > 1:
            stack.pop()

        return ''.join(stack)