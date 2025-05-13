class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0; right = len(matrix) - 1

        while left <= right:
            i = (left + right) // 2

            if matrix[i][0] <= target <= matrix[i][-1]:
                l = 0; r = len(matrix[i]) - 1
                while l <= r:
                    j = (l + r) // 2
                    if matrix[i][j] == target:
                        return True
                    if target <= matrix[i][j]:
                        r = j - 1
                    else:
                        l = j + 1
                return False 

            if target < matrix[i][0]:
                right = i - 1
            elif target > matrix[i][-1]:
                left = i + 1
        return False