class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        l = len(part)
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= l and ''.join(stack[-l:]) == part:
                for _ in range(l):
                    stack.pop()
        return ''.join(stack)