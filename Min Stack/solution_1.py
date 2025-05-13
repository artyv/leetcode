class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack_min or val <= self.getMin():
            self.stack_min.append(val)
        else:
            self.stack_min.append(self.getMin())
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.stack_min.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack_min[-1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()