class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        components = []
        visited = set()

        graph = defaultdict(set)

        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)

        for i in range(n):
            if i not in visited:
                adj_list = []
                queue = deque([i])
                while queue:
                    cur = queue.popleft()
                    visited.add(cur)
                    adj_list.append(cur)

                    for ver in graph[cur]:
                        if ver not in visited:
                            queue.append(ver)
                            visited.add(ver)

                components.append(adj_list)
        
        complete_components = 0
        for c in components:
            counter_edges = 0
            for ver in c:
                counter_edges += len(graph[ver])
            n_c = len(c)
            if (counter_edges) == n_c * (n_c - 1):
                complete_components += 1

        return complete_components
