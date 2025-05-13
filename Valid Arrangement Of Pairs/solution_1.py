class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:  
        # Построение графа
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        # Нахождение стартовой вершины
        start_node = pairs[0][0]
        for node in out_degree:
            if out_degree[node] > in_degree[node]:
                start_node = node
                break

        # Эйлеров путь (обход графа)
        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
                path.append((node, next_node))

        path = []
        dfs(start_node)

        # Результат в правильном порядке
        return path[::-1]

