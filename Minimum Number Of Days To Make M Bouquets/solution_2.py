class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        elif m * k == len(bloomDay):
            return max(bloomDay)
        
        def is_possible(number_of_days):
            bouquets, flowers = 0, 0
            for x in bloomDay:
                if x > number_of_days:
                    flowers = 0
                else:
                    flowers += 1
                    bouquets += flowers // k
                    flowers = flowers % k
            return bouquets >= m

        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = (l+r) // 2
            if is_possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


