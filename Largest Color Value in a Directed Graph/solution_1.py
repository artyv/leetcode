class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        in_degree = [0] * n

        for u,v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        dp = [[0] * 26 for _ in range(n)]

        q = deque()
        for node in range(n):
            if in_degree[node] == 0:
                color = ord(colors[node]) - ord('a')
                dp[node][color] = 1
                q.append(node)
        
        # Need to check for cycles
        processed = 0
        while q:
            u = q.popleft()
            processed += 1
            for v in graph[u]:
                for c in range(26):
                    add = 1 if ord(colors[v]) - ord('a') == c else 0
                    dp[v][c] = max(dp[v][c], dp[u][c] + add)
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        if processed < n:
            return -1

        return max(max(row) for row in dp) # max count of any color along any path
