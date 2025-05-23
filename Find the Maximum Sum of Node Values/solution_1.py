class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        total = sum(nums)
        gains = []

        for x in nums:
            gains.append((x ^ k) - x)

        gains.sort(reverse=True)

        best = total
        current_gain = 0

        # only even
        for i in range(0, n, 2):
            if i + 1 >= n:
                break
            current_gain += gains[i] + gains[i + 1]
            best = max(best, total + current_gain)

        return best
    
