class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        max_mind = 1
        l, r = 1, position[-1] - position[0]
        while l <= r:
            mid = l + (r-l) // 2
            if self.is_possible(position, mid, m):
                max_mind = mid
                l = mid + 1
            else:
                r = mid - 1
        return max_mind

    def is_possible(self, my_list, distance, n_balls):
        balls = 1; prev = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] - prev >= distance:
                prev = my_list[i]
                balls += 1
                if balls == n_balls:
                    return True
        return False
            