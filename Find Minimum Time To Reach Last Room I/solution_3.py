class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        inf = float('inf')
        d = [[inf] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        d[0][0] = 0

        heap = [(0, 0, 0)]  # (time, x, y)

        while heap:
            time, x, y = heapq.heappop(heap)
            if visited[x][y]:
                continue
            visited[x][y] = True

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    arrival = max(time, moveTime[nx][ny]) + 1
                    if d[nx][ny] > arrival:
                        d[nx][ny] = arrival
                        heapq.heappush(heap, (arrival, nx, ny))

        return d[n-1][m-1]