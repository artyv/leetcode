class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        counter = sum(x != y for x,y in zip(heights, expected))
        return counter