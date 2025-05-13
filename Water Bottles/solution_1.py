class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        counter = numBottles
        balance = numBottles
        while balance >= numExchange:
            balance -= numExchange - 1
            counter += 1
        return counter
