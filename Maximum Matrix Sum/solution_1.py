class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        xmin = 10**10
        count_neg = 0

        for row in matrix:
            for x in row:
                total_sum += abs(x)
                if x < 0:
                    count_neg += 1
                xmin = min(xmin, abs(x))
        
        if count_neg % 2 != 0:
            total_sum -= 2 * xmin
        
        return total_sum