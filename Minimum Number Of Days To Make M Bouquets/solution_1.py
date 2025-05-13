class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        elif m * k == len(bloomDay):
            return max(bloomDay)
        
        bouquets = sorted([(max(bloomDay[i:i+k]), i) for i in range(len(bloomDay)-k+1)])
        print(bouquets)

        min_days = 0
        prev = [-k]

        for t in bouquets:
            if all(abs(t[1] - x) >= k for x in prev):
                min_days = max(min_days, t[0])
                prev.append(t[1])
                m -= 1
            if m == 0:
                return min_days

        return -1