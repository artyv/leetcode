class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split('/'):
            if part == '..' and stack:
                stack.pop()
            elif part not in ('..', '.', ''):
                stack.append(part)
        
        return '/'+'/'.join(stack)