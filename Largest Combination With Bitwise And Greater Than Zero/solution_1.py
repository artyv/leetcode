class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = [0] * 24
        for i in range(24):
            for x in candidates:
                if (x & (1 << i)) != 0:
                    count[i] += 1
        return max(count)
                