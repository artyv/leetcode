class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        l = len(gas)
        aux = [-1] * l

        for i in range(l):
            aux[i] = gas[i] - cost[i]

        balance = 0
        index = aux.index(max(aux))

        for i in range(index, l):
            balance += aux[i]

            if balance < 0:
                balance = 0
                index = i + 1
        return index % l