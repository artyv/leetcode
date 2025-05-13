class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        xmin1 = 10**10; xmin2 = 10**10
        xmax1 = -10**9; xmax2 = -10**9
        index_min = -1; index_max = -1

        for i, x in enumerate(arrays):
            if x[0] < xmin1:
                xmin2 = xmin1
                xmin1 = x[0]
                index_min = i
            elif x[0] < xmin2:
                xmin2 = x[0]
            
            if x[-1] > xmax1:
                xmax2 = xmax1
                xmax1 = x[-1]
                index_max = i
            elif x[-1] > xmax2:
                xmax2 = x[-1]
        
        if index_min != index_max:
            return abs(xmax1 - xmin1)
        else:
            return max(abs(xmax1-xmin2), abs(xmax2-xmin1))