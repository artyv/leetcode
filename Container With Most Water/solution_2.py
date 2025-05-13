class Solution:
    def maxArea(self, height: List[int]) -> int:
        vmax, i, j = 0, 0, len(height) - 1

        while i < j:
            vmax = max(vmax, (j-i)*min(height[i], height[j]))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return vmax