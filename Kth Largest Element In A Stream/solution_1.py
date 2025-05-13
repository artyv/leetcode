class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = sorted(nums, reverse=True)[:self.k]

    def add(self, val: int) -> int:
        if self.heap and val > self.heap[-1]:
            for i in range(self.k):
                if val >= self.heap[i]:
                    self.heap.insert(i, val)
                    break
            self.heap.pop()
        if self.heap:
            return self.heap[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)