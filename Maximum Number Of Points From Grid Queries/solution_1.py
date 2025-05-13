class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n  = len(grid), len(grid[0])
        queries_sorted = sorted([(x, i) for (i, x) in enumerate(queries)])
        answer = [0] * len(queries)

        min_heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        available_points = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for q, i in queries_sorted:
            while min_heap and min_heap[0][0] < q:
                val, x, y = heappop(min_heap)
                available_points += 1

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        heappush(min_heap, (grid[nx][ny], nx, ny))
            
            answer[i] = available_points
        
        return answer