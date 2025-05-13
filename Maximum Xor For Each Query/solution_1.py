class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        dq = deque()
        xor = 0; xmax = 2**maximumBit - 1
        for x in nums:
            xor ^= x
            dq.appendleft(xmax ^ xor)
        return list(dq)
