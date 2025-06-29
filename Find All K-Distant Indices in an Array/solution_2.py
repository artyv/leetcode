class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        mark = [0] * n
        lower, high = 0, n-1
        
        for i, val in enumerate(nums):
            if val == key:
                for j in range(max(lower, i-k), min(high, i+k) + 1):
                    mark[j] = 1

        return [i for i, v in enumerate(mark) if v]
