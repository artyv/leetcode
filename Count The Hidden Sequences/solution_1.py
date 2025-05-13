class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # x x+1 x-2 x+4
        # 1 <= x-2 and x+2 <= 6
        # 3 <= x <= 4
        x_min = x_max = 0
        cur = 0
        for x in differences:
            cur += x
            x_min = min(x_min, cur)
            x_max = max(x_max, cur)
        
        variations = (upper - x_max) - (lower - x_min) + 1
        return variations if variations > 0 else 0