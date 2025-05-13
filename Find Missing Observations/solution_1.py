class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        balance = 0
        for x in rolls:
            balance += x - mean
        
        xmax = 6; xmin = 1
        res = [mean] * n
        if balance == 0:
            return res
        elif balance < 0:
            delta = xmax
        else:
            delta = xmin
        
        if abs(balance) > n * abs(mean-delta):
            return []
        
        for i in range(n):
            if abs(balance) <= abs(mean-delta):
                res[i] = mean - balance
                return res
            res[i] = delta
            balance -= mean - delta
        return res