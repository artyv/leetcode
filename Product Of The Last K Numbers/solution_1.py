class ProductOfNumbers:

    def __init__(self):
        self.partial = [1]
        self.l = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.partial = [1]
            self.l = 0
        else:
            self.partial.append(num*self.partial[-1])
            self.l += 1

    def getProduct(self, k: int) -> int:
        return self.partial[-1] // self.partial[self.l-k] if k <= self.l else 0
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)