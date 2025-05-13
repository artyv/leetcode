class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        path_sum = [triangle[0]]

        for row in range(1, len(triangle)):
            temp = [triangle[row][0] + path_sum[row-1][0]]
            temp.extend([triangle[row][j] + min(path_sum[row-1][j], path_sum[row-1][j-1]) for j in range(1, len(triangle[row-1]))])
            temp.extend([triangle[row][-1] + path_sum[row-1][-1]])
            path_sum.append(temp)
        return min(path_sum[-1])
