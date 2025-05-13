class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)

        for u,v,time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        dist = [float('inf')] * n  # Min time to each v
        dist[0] = 0
        
        ways = [0] * n  # Number of shortest paths to each v
        ways[0] = 1

        heap = [(0, 0)]

        while heap:
            cur_time, node = heappop(heap)

            if cur_time > dist[node]:
                continue

            for neighbor, travel_time in graph[node]:
                new_time = cur_time + travel_time

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heappush(heap, (new_time, neighbor))
                
                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]