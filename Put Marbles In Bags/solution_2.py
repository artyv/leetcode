class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairs_weight = []
        heapq.heapify(pairs_weight)

        for i in range(n-1):
            heapq.heappush(pairs_weight, (weights[i] + weights[i+1]))
        
        return sum(heapq.nlargest(k-1, pairs_weight)) - sum(heapq.nsmallest(k-1, pairs_weight))



        