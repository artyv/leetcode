class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)

        freq = dict()
        counter = 0

        for i in range(n):
            for j in range(i+1, n):
                value = nums[i] * nums[j]
                if value in freq:
                    freq[value] += 1
                else:
                    freq[value] = 1
        for f in freq.values():
            pairs = (f - 1) * f // 2
            counter += 8 * pairs
        
        return counter