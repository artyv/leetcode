class Solution:
    def maxArea(self, height: List[int]) -> int:
        vmax, i, j = 0, 0, len(height) - 1

        while i < j:
            h = min(height[i], height[j])
            vmax = max(vmax, (j-i)*h)
            while height[i] <= h and i < j:
                i += 1
            while h >= height[j] and i < j:
                j -= 1
        return vmax