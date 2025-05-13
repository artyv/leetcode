from itertools import accumulate

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        aux = [-1] * 2 * l

        for i in range(l):
            aux[i] = gas[i] - cost[i]
            aux[i+l] = gas[i] - cost[i]

        for i in range(l):
            if aux[i] < 0:
                continue
            if i < l - 1 and aux[i] == 0:
                continue
            score = aux[i]
            for j in range(i + 1, i + l):
                score += aux[j]
                if score < 0:
                    break
            if score >= 0:        
                return i
        return -1