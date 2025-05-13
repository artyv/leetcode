class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split('/'):
            if stack and part == '..':
                stack.pop()
            elif part not in ('..', '.', ''):
                stack.append(part)
        
        return '/'+'/'.join(stack)