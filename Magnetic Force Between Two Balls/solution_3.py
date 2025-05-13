class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        selected_baskets = [min(position), max(position)]
        x_to_add = 0
        max_mindiff = max(position) - min(position)
        for _ in range(m-2):
            temp_diff = 0
            for x in position:
                min_distance = min(abs(x-y) for y in selected_baskets)
                if min_distance > temp_diff:
                    x_to_add = x
                    max_mindiff = min_distance
            selected_baskets.append(x_to_add)
        return max_mindiff