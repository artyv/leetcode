class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        timer = 0; waiting = 0
        for a, b in customers:
            if timer > a: # starts later than the person arrived
                waiting += timer - a
            else: # idle until moment a
                timer = a
            waiting += b
            timer += b
        return waiting/len(customers)