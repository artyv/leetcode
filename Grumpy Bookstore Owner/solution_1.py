class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = len(customers)

        counter = sum(customers[:minutes])
        for i in range(minutes, l):
            if grumpy[i] == 0:
                counter += customers[i]
        
        cmax = counter
        
        for i in range(1, l-minutes+1):
            if grumpy[i-1] == 1:
                counter -= customers[i-1]
            if grumpy[i+minutes-1] == 1:
                counter += customers[i+minutes-1]
            
            cmax = max(cmax, counter)
        return cmax