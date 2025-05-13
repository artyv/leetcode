class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        timer = customers[0][0]
        waiting = 0
        for a, b in customers:
            if timer > a:
                waiting += timer - a
            waiting += b
            timer += b
        return waiting/len(customers)