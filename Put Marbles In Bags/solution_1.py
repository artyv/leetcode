class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairs_weight = [weights[i] + weights[i+1] for i in range(n-1)]

        pairs_weight.sort()
        
        return sum(pairs_weight[-(k-1):]) - sum(pairs_weight[:(k-1)])



        