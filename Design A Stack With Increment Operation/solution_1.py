class CustomStack:

    def __init__(self, maxSize: int):
        self.my_list = []
        self.size_max = maxSize

    def push(self, x: int) -> None:
        if len(self.my_list) < self.size_max:
            self.my_list.append(x)

    def pop(self) -> int:
        if self.my_list:
            return self.my_list.pop(-1)
        return -1
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.my_list))):
            self.my_list[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)