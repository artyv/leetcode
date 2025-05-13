class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, min(ranks) * cars**2

        while l < r:
            mid = (l + r) // 2

            num_cars = 0
            for x in ranks:
                num_cars += floor(sqrt(mid / x))
            
            if num_cars >= cars:
                r = mid
            else:
                l = mid + 1
        
        return l