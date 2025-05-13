class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for x in nums:
            xor ^= x
        rightmost_set_bit = xor & -xor

        ones = 0; zeros = 0
        for x in nums:
            if x & rightmost_set_bit:
                ones ^= x
            else:
                zeros ^= x
        return [ones, zeros]