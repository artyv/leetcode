class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0; right = len(matrix) - 1

        while left <= right:
            i = (left + right) // 2

            if matrix[i][0] <= target <= matrix[i][-1]:
                index = bisect.bisect_left(matrix[i], target)
                if matrix[i][index] == target:
                    return True
                else:
                    return False

            if target < matrix[i][0]:
                right = i - 1
            elif target > matrix[i][-1]:
                left = i + 1
        return False