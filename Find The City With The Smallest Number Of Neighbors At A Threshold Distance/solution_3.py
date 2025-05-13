class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[float('inf')] * n for _ in range(n)]
        
        for e in edges:
            distance[e[0]][e[1]] = e[2]
            distance[e[1]][e[0]] = e[2]
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        
        print(distance)
        answer = -1
        city_min = 10**10

        for i in range(n):
            counter = 0
            for j in range(n):
                if distance[i][j] <= distanceThreshold and i != j:
                    counter += 1
            
            if counter <= city_min:
                answer = i
                city_min = counter
        
        return answer