class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 1; r = position[-1] - position[0]
        max_mind = -1
        leng = len(position)

        while l <= r:
            mid = l + (r-l) // 2
            balls = 1; prev = position[0]
            for i in range(1, leng):
                if position[i] - prev >= mid:
                    prev = position[i]
                    balls += 1
                    if balls >= m:
                        max_mind = mid
                        l = mid + 1
                        break
            else:
                r = mid - 1
        
        return max_mind
            