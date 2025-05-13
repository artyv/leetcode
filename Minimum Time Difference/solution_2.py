class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        tmin1 = tmin2 = '23:59'
        tmax1 = tmax2 = '00:00'

        for t in timePoints:
            if t < tmin1:
                tmin2 = tmin1
                tmin1 = t
            elif t < tmin2:
                tmin2 = t
            
            if t > tmax1:
                tmax2 = tmax1
                tmax1 = t
            elif t > tmax2:
                tmax2 = t

        t1 = 60 * int(tmax1[:2]) + int(tmax1[3:]) - 60 * int(tmax2[:2]) - int(tmax2[3:])
        t2 = 60 * int(tmin2[:2]) + int(tmin2[3:]) - 60 * int(tmin1[:2]) - int(tmin1[3:])
        t3 = 24*60 + 60 * int(tmin1[:2]) + int(tmin1[3:]) - 60 * int(tmax1[:2]) - int(tmax1[3:])
        return min(t1, t2, t3)
