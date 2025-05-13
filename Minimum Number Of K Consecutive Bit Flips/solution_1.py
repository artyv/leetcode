class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flips = 0; l = len(nums)
        flipped = 0
        aux = [0] * l
        for i in range(l):
            if i >= k:
                flipped ^= aux[i-k]
            if flipped == nums[i]:
                if i + k > l:
                    return -1
                aux[i] = 1
                flipped ^= 1
                flips += 1

        return flips