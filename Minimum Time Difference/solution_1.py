class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        tmin = 10**10
        timePoints.sort()
        timePoints.append(str(int(timePoints[0][:2]) + 24) + timePoints[0][2:])

        for i in range(1, len(timePoints)):
            temp = 60*int(timePoints[i][:2]) + int(timePoints[i][3:]) - 60*int(timePoints[i-1][:2]) - int(timePoints[i-1][3:])
            tmin = min(tmin, temp)
        return tmin
    
